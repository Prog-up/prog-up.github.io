### Managing Firmware on Linux with `fwupd`

On Linux, system and device firmware is managed through **fwupd**. Many Linux users overlook firmware updates, leaving their BIOS, SSDs, and peripherals out of date.

#### How to update firmware

On GNOME and KDE, **GNOME Software** and **Discover** handle firmware updates automatically in the UI. 

From the terminal:
```bash
fwupdmgr refresh && fwupdmgr get-updates
fwupdmgr update
```

### NVIDIA joins LVFS as Premier Sponsor

Despite keeping their graphics drivers closed source, NVIDIA is now contributing $100k+ annually to the Linux Vendor Firmware Service (LVFS). This covers DGX system firmware updates, with potential support for graphics cards in the future.

![LVFS](/assets/cases/lvfs/image.webp)

<div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
<a href="https://www.phoronix.com/news/NVIDIA-Premier-Sponsor-LVFS" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">Source from Phoronix</a>
<a href="https://wiki.archlinux.org/title/Fwupd" target="_blank" class="button pill mt-2" style="display:inline-block; text-decoration:none;">More about fwupd on ArchWiki</a>
</div>


