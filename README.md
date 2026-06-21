# IterationRP Edit - V2.3 Patch
For my configuration settings, download txt file and place in same folder as the shaders
This repository provides a patch for the **IterationRP Alpha 0.8.23** shader pack. Due to licensing, the original shader code cannot be distributed directly. Users must own the original shader zip to apply this edit.
## New in v2.2
- **performance optimazations** Should gain ~15 fps from previous version and should be stable and dont go below 60fps while using fsr balanced on 1440p resolution+
## New in v2.2
- **better moon and night sky textures**
- **dynamic moonphase lighting intesity during night**
- **SEUS inspired preset tonemaping for opendrt**
- **ability to make custom preset for opendrt**
## New in V2.1
- **suport for ocean physics and physics mod**
## New in V2.0
- **changed build structure from old 0.8.18 to newest 0.8.23**
- **Better dual lobe system**
- **mostly all relevant features from previous edits, but porting takes time and this is still work in progress**
- **OpenDRT support based on https://github.com/JElfferich/itrp-patches patches**
- **ALL benefits of using new version (0.8.23) as base. So Transparency fix, better denoiser, and so on** 

## New in V1.19
- **Revelation (shader) inspired cloud *coverage* map with localized clouds (no longer having overcast everywhere, or having one part clear while other has broken clouds)**
- **Cloud Shadows distance from player** (how far from player they appear)
## New in V1.18
- **Pixelated clouds optinality :D** similar to the Euphoria Patches
- **nice chatgpt writen descriptions of things i made cos im not doing this sh*t**
## New in V1.17 - hotfix denoiser (dont turn off normal bloom)
- **Ported Convolution Bloom from huj's patches [huj31415/iterationrp-patches](https://github.com/huj31415/iterationrp-patches)**
- **he is a goat**
- **if u are intrested about ading custom kernels (the look of conv bloom) please check his repo and his tool**
- **added some minor improvements, and aditional settings to cycle betwen custom kernels**
- **changed deafult settings to much more playable/refined experience**
## New in V1.16
- **HUGE performance boost compared to last version**
- **Flicker for light (torches, etc.)**
- **aurora colors - for now no dynamic so u need to change it manually**
- **lighleak fix - fix** //better lightleak fix behaviour during sunrize and sunset and mismatch betwen godrays and highlights
- **enabled color stained godrays by deafult**
## New in V1.15
- **added wave simulation from Eclipse Shader**
- **added profiles for settings *Original, Edit* as well for clouds style *Original, Edit, Original with Dynamic Weather*. For best experience i recomed using "Shaders Profiles" mod from modrinth**
## New in V1.14
-added Dust Motes 
- **hotfix for 1.13 hdr clamping at 216 nits**
## New in V1.13
- **multiple visual fixes**
- **cloud edhes wisp and hair effects** 
## New in V1.12
- **integrated the IterationRp 0.8.22 changes to the patches so now its deafult version for V1.12+**
- **Hdr support and transparency fix from original**
## New in V1.11
- **new deafult options so dont use old, it might look bad**
- **reworked cloud erosion (cloud scattering) and Cloud look (if u dont like it use V1.10)**
- **added sunset exposure toggle for deafult exposure behaviour during sunset**
## New in V1.10
- **Aurora Borealis System**: High-fidelity, performance-optimized dynamic aurora with organic movement.
- **Aurora Settings**: Dedicated AURORA tab in the menu with controls for master toggle, probability (frequency), and biome restriction (Snowy/Desert).
- **Atmospheric Storm Darkening**: Re-tuned cloud density and light absorption to provide a cinematic "blackout" effect during thunderstorms.
- **Cloud Animation Toggle**: New setting in the Volumetric Clouds menu to switch between **Frame Time** (continuous movement) and **World Time** (movement tied to in-game ticks).
- **Time Source Stability**: Fixed flickering and precision artifacts when using world-time synchronized clouds.
- CLOUDS ARE NO LONGER CLIPING THRU LODS AND THEY ARE FULLY FLYABLE IN OR WHATEVER!!!!!!
  
## Previous Changes (V1.04)
Dynamic Cloud System with different weathers
Reworked Godrays and Cloud Shadows
Cloud Godrays (similar to fog godrays but implemented into clouds for beautiful highlights)
Tweaked Cloud Visuals (Better scattered/planar clouds, more variations and randomness)
Flares (Both Anamorphic and Entopic)
Rainbows
Time Grade
Custom LUTs
Film Grain based on RGB noise
SSS Edits
Dynamic Biome color grading
Bokeh styles for Depth of field

## How to Apply the Patch

### Requirements
- Python 3.x installed.
- Git installed (for `git apply` functionality).
- The original `iterationRP Alpha 0.8.22.zip` file.

### Instructions
1. Download `shader-patch.py` and `ITRPeditV1.15.diff` from this repository.
2. Place the original `iterationRP Alpha 0.8.22.zip` in the same folder.
3. Open a terminal/command prompt in that folder.
4. Run the following command:

```bash
python shader-patch.py "iterationRP Alpha 0.8.18.zip" "ITRPeditV1.11.diff" "ITRPedit_V1.11.zip"
```
or for the V1.12+ using 0.8.22+
```bash
python shader-patch.py "iterationRP Alpha (version).zip" "ITRPeditV(version).diff" "ITRPedit_V(version).zip"
```

5. The patched shader pack will be generated as `ITRPedit_V1.11.zip`/`ITRPedit_V(version).zip`. You can now move this into your Minecraft `shaderpacks` folder.

## Credits
- Original Shader: [IterationRP](https://github.com/Tahnass/IterationRP)
- Patching Script based on: [huj31415/iterationrp-patches](https://github.com/huj31415/iterationrp-patches)
- OpenDrt support creator: [JElfferich Jordy Elfferich](https://github.com/JElfferich/itrp-patches)
