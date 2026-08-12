# Open Duck Mini Printing Progress

This tracker follows the upstream Open Duck Mini v2 print guide and gives me a simple daily checklist for printing, checking, and photographing each part.

Upstream source: https://github.com/apirrone/Open_Duck_Mini/blob/v2/docs/print_guide.md

## Default Print Settings

- Printer: Bambu Lab P1S
- Slicer: Bambu Studio
- Default material: PLA
- Default infill: 15%
- Photo folder: `photos/printing/`

## Foot Bottom Note

The upstream guide lists both `foot_bottom_pla.stl` and `foot_bottom_tpu.stl`.

- Use `foot_bottom_pla.stl` as the PLA-friendly starter option.
- Treat `foot_bottom_tpu.stl` as optional for later, printed in TPU at 40% infill for better grip.

## Feet

- [x] `foot_top.stl` x2
- [x] `foot_side.stl` x2
- [x] `foot_bottom_pla.stl` x2
- [ ] `foot_bottom_tpu.stl` x2 - optional, TPU at 40% infill

## Legs

- [ ] `knee_to_ankle_left_sheet.stl` x4
- [ ] `knee_to_ankle_right_sheet.stl` x4
- [x] `leg_spacer.stl` x4
- [ ] `left_roll_to_pitch.stl` x1
- [ ] `right_roll_to_pitch.stl` x1
- [ ] `roll_motor_bottom.stl` x2
- [ ] `roll_motor_top.stl` x2

## Trunk

- [ ] `trunk_bottom.stl` x1
- [ ] `trunk_top.stl` x1

## Neck

- [ ] `neck_left_sheet.stl` x1
- [ ] `neck_right_sheet.stl` x1

## Head

- [ ] `head_pitch_to_yaw.stl` x1
- [ ] `head_yaw_to_roll.stl` x1
- [ ] `head_roll_mount.stl` x1
- [ ] `head.stl` x1
- [ ] `head_bot_sheet.stl` x1
- [ ] `left_antenna_holder.stl` x1
- [ ] `right_antenna_holder.stl` x1
- [ ] `left_eye.stl` x1
- [ ] `right_eye.stl` x1

## Body

- [ ] `left_cache.stl` x1
- [ ] `right_cache.stl` x1
- [ ] `body_front.stl` x1
- [ ] `body_middle_bottom.stl` x1
- [ ] `body_middle_top.stl` x1
- [ ] `body_back.stl` x1
- [ ] `battery_pack_lid.stl` x1

## Accessories

- [ ] `bulb.stl` x1
- [ ] `flash_light_module.stl` x1
- [ ] `flash_reflector_interface.stl` x1
- [ ] `speaker_interface.stl` x1
- [ ] `speaker_stand.stl` x1

## Daily Print Notes

Use this section to add a short entry each time I print, reprint, or test-fit parts.

### 2026-08-12

Printed:

- No new printed parts.

Settings:

- Material: PLA foot parts from the previous batch
- Layer height: Not recorded
- Infill: 15%
- Supports: Not recorded
- Plate: Not recorded
- Estimated print time: Not applicable

Result:

- Dry-fitted the PLA foot assemblies without the optional TPU bottoms.
- TPU foot bottoms remain deferred for a later grip upgrade.

Fit check:

- Foot parts lined up well enough for a dry fit with screws.
- Final fit check still depends on adding the TPU bottoms, foot switches, and motors later.

Photos:

- [foot-dry-fit-without-tpu-2026-08-12.jpeg](../photos/printing/feet/foot-dry-fit-without-tpu-2026-08-12.jpeg)

Next:

- Keep the feet assembled for reference, then continue with the next leg components.

### 2026-08-11

Printed:

- `foot_side.stl` x2
- `foot_top.stl` x2
- `foot_bottom_pla.stl` x2

Settings:

- Material: PLA
- Layer height: Not recorded
- Infill: 15%
- Supports: Not recorded
- Plate: Not recorded
- Estimated print time: Not recorded

Result:

- Completed the first full PLA foot print batch.

Fit check:

- Dry fit completed on 2026-08-12 without the optional TPU bottoms.

Photos:

- [foot-side-2026-08-11.jpeg](../photos/printing/feet/foot-side-2026-08-11.jpeg)
- [foot-top-2026-08-11.jpeg](../photos/printing/feet/foot-top-2026-08-11.jpeg)
- [foot-bottom-pla-2026-08-11.jpeg](../photos/printing/feet/foot-bottom-pla-2026-08-11.jpeg)

Next:

- Continue with the next leg components.

### 2026-08-06

Printed:

- `leg_spacer.stl` x4

Settings:

- Material: PLA
- Layer height: Not recorded
- Infill: 15%
- Supports: Not recorded
- Plate: Not recorded
- Estimated print time: Not recorded

Result:

- Completed all four leg spacers.

Fit check:

- Pending screw and assembly fit check.

Photos:

- [leg-spacers-2026-08-06.jpeg](../photos/printing/legs/leg-spacers-2026-08-06.jpeg)

Next:

- Check hole fit and surface cleanup, then continue with the next small leg or foot part.

```markdown
### YYYY-MM-DD

Printed:

- TBD

Settings:

- Material:
- Layer height:
- Infill:
- Supports:
- Plate:
- Estimated print time:

Result:

- TBD

Fit check:

- TBD

Photos:

- TBD

Next:

- TBD
```

## Photo Workflow

- `photos/printing/feet/` - feet and foot pads
- `photos/printing/legs/` - leg linkage and motor mount parts
- `photos/printing/trunk/` - trunk parts
- `photos/printing/neck/` - neck parts
- `photos/printing/head/` - head, eyes, and antenna holders
- `photos/printing/body/` - body panels and battery lid
- `photos/printing/accessories/` - bulb, flash, reflector, speaker parts
- `photos/printing/completed/` - grouped photos of finished print batches
- `photos/printing/failed/` - failed prints and reprint notes
