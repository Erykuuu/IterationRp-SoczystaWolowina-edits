# IterationRP Edit - V1.03 Patch

This repository provides a patch for the **IterationRP Alpha 0.8.18** shader pack. Due to licensing, the original shader code cannot be distributed directly. Users must own the original shader zip to apply this edit.

## Changes in this Edit

Film Grain,
Dynamic Cloud system with diffrent weathers,
Rainbows,
Flares (both Anamorphic and Entopic),
Time Grade,
Custom LUTs,
SSS edits,
Cloud Godrays - similar to fog godrays but implemented to clouds so u get nice highlights,
Cloud Shadows
Reworked Godrays
And some tweaks to overall look of clouds (bettter scatered clouds, better planar clouds, bigger variations and randomness)

## How to Apply the Patch

### Requirements
- Python 3.x installed.
- Git installed (for `git apply` functionality).
- The original `iterationRP Alpha 0.8.18.zip` file.

### Instructions
1. Download `shader-patch.py` and `ITRPeditV1.03.diff` from this repository.
2. Place the original `iterationRP Alpha 0.8.18.zip` in the same folder.
3. Open a terminal/command prompt in that folder.
4. Run the following command:

```bash
python shader-patch.py "iterationRP Alpha 0.8.18.zip" "ITRPeditV1.03.diff" "ITRPedit_V1.03.zip"
```

5. The patched shader pack will be generated as `ITRPedit_V1.03.zip`. You can now move this into your Minecraft `shaderpacks` folder.

## Credits
- Original Shader: [IterationRP](https://github.com/Tahnass/IterationRP)
- Patching Script based on: [huj31415/iterationrp-patches](https://github.com/huj31415/iterationrp-patches)
