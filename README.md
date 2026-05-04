# IterationRP Edit - V1.03 Patch

This repository provides a comprehensive patch for the **IterationRP Alpha 0.8.18** shader pack. Due to licensing, the original shader code cannot be distributed directly. Users must own the original shader zip to apply this edit.

## 🌟 Key Features & Changes

- **Dynamic Cloud System** with different weathers
- **Reworked Godrays** and **Cloud Shadows**
- **Cloud Godrays** (similar to fog godrays but implemented into clouds for beautiful highlights)
- **Tweaked Cloud Visuals** (Better scattered/planar clouds, more variations and randomness)
- **Flares** (Both Anamorphic and Entopic)
- **Rainbows**
- **Time Grade**
- **Custom LUTs**
- **Film Grain based on RGB noise**
- **SSS Edits**

---

## 🛠️ How to Apply the Patch

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

5. The patched shader pack will be generated as `ITRPedit_V1.03.zip`. Move it to your Minecraft `shaderpacks` folder.

## Credits
- Original Shader: [IterationRP](https://github.com/Tahnass/IterationRP) by Tahnass.
- Patching Script based on: [huj31415/iterationrp-patches](https://github.com/huj31415/iterationrp-patches)
