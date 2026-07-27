Most of the conversation around on-device AI centers on Apple Silicon and discrete NVIDIA GPUs. Intel integrated GPUs ship in hundreds of millions of laptops and remain comparatively unstudied, so I spent this semester's technology watch measuring rather than assuming.

I benchmarked 14 text-generation models, from 1B to 9B parameters, across three inference backends on a single Intel Iris Xe laptop: llama.cpp over SYCL, llama.cpp over Vulkan, and the OpenVINO Model Server. Same hardware, same INT4 quantisation, same protocol.

The dominant constraint turned out to be architectural rather than computational. The Xe-LP command streamer caps any single GPU buffer at 4 GiB, which forces the output projection of larger-vocabulary models back onto the CPU under Vulkan and SYCL. OpenVINO's tiled allocation sidesteps that ceiling, and the measured throughput follows directly: on 7B models it reached roughly 12-14 tokens/second against 4-6 for the other two backends.

Serving Gemma 4 exposed a second problem. Its vision-language export ships as a fragmented graph that a production model server cannot load directly. I resolved it by stitching the embedding sub-graphs back into the decoder at the OpenVINO level, producing a single stateful graph that the model server runs at about 14.8 tokens/second on the E4B variant.

Three of the converted models are now public on Hugging Face:
- [Gemma 4V INT4](https://lnkd.in/es6qRH9u)
- [Llama 3 INT4](https://lnkd.in/e6wEjUnM)
- [Mistral 7B INT4](https://lnkd.in/eyNNDr7k)

You can read the full report here:
[View Research Paper (PDF)](/assets/cases/llm-research/Reseach%20Paper.pdf)