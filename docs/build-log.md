# Build Log

This log captures the project as it happens: purchases, prints, mistakes, fixes, calibration notes, and software experiments.

## 2026-08-03 - Repository Scaffold

Status: Phase 1 workshop documentation started.

Notes:

- Created the initial documentation structure for the Open Duck Mini build journal.
- Recorded the Phase 1 workshop tools and consumables discussed so far.
- Added placeholders for photos, CAD modifications, scripts, and BOM tracking.
- Kept attribution to the upstream Open Duck Mini project without copying upstream files.

Next:

- Add photos of the Phase 1 tools.
- Review the official Open Duck Mini BOM.
- Build a Phase 2 shopping list for servos, electronics, power, bearings, and remaining hardware.

## 2026-08-05 - Phase 1 Inventory Photos

Status: Phase 1 physical inventory photographed and added to the repository.

What changed:

- Added photos for the soldering station, wire stripper, calipers, heat-set inserts, screw assortment, solder, desoldering tools, tweezers, heat shrink, silicone wire, and cable ties.
- Updated the Phase 1 workshop notes with the exact purchased items visible in the inventory photos.
- Expanded the Phase 1 checklist so it can be used as a more accurate local inventory.

What I learned:

- The workshop is now ready for printing, fitting, soldering, and basic electrical prep.

Next:

- Begin printing low-risk PLA parts and record progress in `docs/printing-progress.md`.

## 2026-08-06 - First Leg Spacers Printed

Status: First Open Duck Mini printed parts completed.

What changed:

- Printed all four `leg_spacer.stl` parts.
- Added the leg spacer photo to `photos/printing/legs/`.
- Marked `leg_spacer.stl` complete in the printing progress tracker.

What I learned:

- The project has moved from workshop setup into real robot part production.

Problems:

- Print settings beyond PLA and 15% infill were not recorded for this batch.

Next:

- Check the leg spacer holes and cleanup quality before printing the next batch.

## 2026-08-11 - PLA Foot Parts Printed

Status: First full foot batch printed in PLA.

What changed:

- Printed `foot_side.stl` x2.
- Printed `foot_top.stl` x2.
- Printed `foot_bottom_pla.stl` x2.
- Added foot print photos to `photos/printing/feet/`.
- Marked the PLA foot parts complete in the printing progress tracker.

What I learned:

- The feet can now be dry-fitted before deciding whether TPU foot bottoms are needed later.

Problems:

- Print settings beyond PLA and 15% infill were not recorded for this batch.

Next:

- Dry fit the printed foot parts, clean up holes if needed, and continue with the next leg components.

## 2026-08-12 - Feet Dry Fit

Status: PLA feet dry-fitted without TPU bottoms.

What changed:

- Dry-fitted the printed `foot_side.stl`, `foot_top.stl`, and `foot_bottom_pla.stl` parts.
- Added the dry-fit photo to `photos/printing/feet/`.
- Updated the printing tracker to record that TPU bottoms are still deferred for later.

What I learned:

- The printed PLA foot parts line up well enough to assemble as a dry fit.

Problems:

- TPU bottoms, foot switches, and motors are still missing, so this is not the final foot assembly.

Next:

- Keep the feet as a reference assembly and continue printing the next leg components.

## 2026-08-12 - Knee-To-Ankle Sheets Printed

Status: Main knee-to-ankle sheet batch completed.

What changed:

- Printed `knee_to_ankle_left_sheet.stl` x4.
- Printed `knee_to_ankle_right_sheet.stl` x4.
- Added the leg sheet photo to `photos/printing/legs/`.
- Marked both knee-to-ankle sheet entries complete in the printing progress tracker.

What I learned:

- The leg print batch is now moving beyond small test pieces into the repeated structural parts.

Problems:

- Fit check with the leg spacers, motor mounts, and hardware is still pending.

Next:

- Print `roll_motor_bottom.stl` x2 and `roll_motor_top.stl` x2, then start checking the leg subassembly fit.

## 2026-08-13 - Roll Motor Mounts Printed

Status: Roll motor top and bottom parts printed.

What changed:

- Printed `roll_motor_top.stl` x2.
- Printed `roll_motor_bottom.stl` x2 after orientation/support issues on earlier attempts.
- Added roll motor print and cleanup photos to `photos/printing/legs/`.
- Marked both roll motor entries complete in the printing progress tracker.
- Updated README progress to include the new printed parts.

What I learned:

- `roll_motor_bottom.stl` needs careful orientation and gentle support removal because the geometry is easy to damage.

Problems:

- Support removal was rough on `roll_motor_bottom.stl`; the parts still need fit-checking before final use.

Next:

- Print `left_roll_to_pitch.stl` x1 and `right_roll_to_pitch.stl` x1.

## 2026-08-14 - Trunk Top And Bottom Printed

Status: Main trunk pieces printed.

What changed:

- Printed `trunk_bottom.stl` x1.
- Printed `trunk_top.stl` x1.
- Added trunk print photos to `photos/printing/trunk/`.
- Marked both trunk entries complete in the printing progress tracker.
- Updated README progress to include the trunk pieces.

What I learned:

- The build is now moving from repeated leg parts into the central torso structure.

Problems:

- Fit check with the leg assemblies, servos, controller board, Raspberry Pi, and wiring is still pending.

Next:

- Roll-to-pitch parts completed later on 2026-08-14; print the neck sheets next.

## 2026-08-14 - Roll-To-Pitch Parts Printed

Status: Left and right roll-to-pitch parts printed.

What changed:

- Printed `left_roll_to_pitch.stl` x1.
- Printed `right_roll_to_pitch.stl` x1.
- Added roll-to-pitch photos to `photos/printing/legs/`.
- Corrected the previously misplaced roll-to-pitch side-view photo so it is linked from the right print entry.
- Marked both roll-to-pitch entries complete in the printing progress tracker.
- Updated README progress to include the completed leg print group.

What I learned:

- The required leg print group is now complete enough for dry fitting and later servo checks.

Problems:

- Fit check with the servos and hardware is still pending.

Next:

- Print `neck_left_sheet.stl` x1 and `neck_right_sheet.stl` x1.

## 2026-08-14 - Neck Sheets Printed

Status: Neck sheets printed and screw holes checked.

What changed:

- Printed `neck_left_sheet.stl` x1.
- Printed `neck_right_sheet.stl` x1.
- Added the neck sheet photo to `photos/printing/neck/`.
- Marked both neck sheet entries complete in the printing progress tracker.
- Updated README progress to include the neck sheets.

What I learned:

- These parts are not perfect cosmetically, but the screw holes were checked and should work for now.

Problems:

- Rough areas around some holes and cut-outs should be watched during final neck/head fit checking.

Next:

- Print `head_pitch_to_yaw.stl` x1 and `head_yaw_to_roll.stl` x1.

## 2026-08-14 - Head Pitch/Yaw Linkage Printed

Status: First head linkage parts printed.

What changed:

- Printed `head_pitch_to_yaw.stl` x1.
- Printed `head_yaw_to_roll.stl` x1.
- Added the head linkage photos to `photos/printing/head/`.
- Marked both head linkage entries complete in the printing progress tracker.
- Updated README progress to include the first head parts.

What I learned:

- The build has moved from neck support pieces into the head mechanism.

Problems:

- Fit check with the neck sheets, head roll mount, head servos, and hardware is still pending.

Next:

- Print `head_roll_mount.stl` x1 and `head_bot_sheet.stl` x1.

## 2026-08-14 - Head Roll Mount And Bottom Sheet Printed

Status: Head support parts printed.

What changed:

- Printed `head_roll_mount.stl` x1.
- Printed `head_bot_sheet.stl` x1.
- Added the head support photos to `photos/printing/head/`.
- Marked both head support entries complete in the printing progress tracker.
- Updated README progress to include these head parts.

What I learned:

- Most of the head mechanism support pieces are now printed; the larger head shell is the next main print.

Problems:

- Fit check with the head shell, head servos, neck linkage, and hardware is still pending.

Next:

- Print `head.stl` x1.

## 2026-08-15 - Head Shell Printed

Status: Main head shell printed.

What changed:

- Printed `head.stl` x1.
- Added the head shell photo to `photos/printing/head/`.
- Marked the head shell complete in the printing progress tracker.
- Updated README progress to include the new head print.

What I learned:

- The upper-body print set is now far enough along that the head details are the next logical small batch.

Problems:

- Fit check with the head bottom sheet, head roll mount, head servos, antenna holders, eyes, and hardware is still pending.

Next:

- Print `left_antenna_holder.stl` x1, `right_antenna_holder.stl` x1, `left_eye.stl` x1, and `right_eye.stl` x1.

## 2026-08-15 - Head Details Printed

Status: Required head print group completed.

What changed:

- Printed `left_antenna_holder.stl` x1.
- Printed `right_antenna_holder.stl` x1.
- Printed `left_eye.stl` x1.
- Printed `right_eye.stl` x1.
- Added the antenna holder and eye photos to `photos/printing/head/`.
- Marked the four head detail parts complete in the printing progress tracker.
- Updated README progress to include the completed head group.

What I learned:

- The required head print group is now complete, so the next useful batch is the body/cache pieces.

Problems:

- Fit check with the head shell, head bottom sheet, head servos, antenna hardware, and eye mounting hardware is still pending.

Next:

- Print `left_cache.stl` x1 and `right_cache.stl` x1, then continue into the body panels.

## 2026-08-16 - Left And Right Cache Pieces Printed

Status: First body/cache pieces printed.

What changed:

- Printed `left_cache.stl` x1.
- Printed `right_cache.stl` x1.
- Added the cache piece photos to `photos/printing/body/`.
- Marked both cache parts complete in the printing progress tracker.
- Updated README progress to include the new body pieces.

What I learned:

- Support contact areas on these cosmetic body pieces may need sanding and cleaning before they look acceptable.
- The finish is not ideal, but these areas should be fine to paint over later.

Problems:

- Support cleanup left some visible finish issues.
- Final fit with the body panels, trunk pieces, hardware, and electronics is still pending.

Next:

- Print `body_front.stl` x1, then continue with `body_middle_bottom.stl` and `body_middle_top.stl`.

## 2026-08-16 - Body Front Panel Printed

Status: Body front panel printed.

What changed:

- Printed `body_front.stl` x1.
- Added the body front photo to `photos/printing/body/`.
- Marked the body front panel complete in the printing progress tracker.
- Updated README progress to include the new body panel.

What I learned:

- The body print group is now underway beyond the cache pieces.

Problems:

- Final fit with the cache pieces, middle body panels, body back, trunk pieces, hardware, and electronics is still pending.

Next:

- Print `body_middle_bottom.stl` x1 and `body_middle_top.stl` x1.

## 2026-08-17 - Body Middle Bottom Panel Printed

Status: Body middle bottom panel printed.

What changed:

- Printed `body_middle_bottom.stl` x1.
- Added the body middle bottom photo to `photos/printing/body/`.
- Marked the body middle bottom panel complete in the printing progress tracker.
- Updated README progress to 41 / 49 required printed parts.

What I learned:

- The middle body shell is now underway, with the top panel still remaining.

Problems:

- Final fit with the body middle top, body back, battery lid, trunk pieces, hardware, servos, and electronics is still pending.

Next:

- Print `body_middle_top.stl` x1, then continue with `body_back.stl`.

## 2026-08-18 - Body Middle Top Panel Printed

Status: Body middle top panel printed.

What changed:

- Printed `body_middle_top.stl` x1.
- Added the body middle top photo to `photos/printing/body/`.
- Marked the body middle top panel complete in the printing progress tracker.
- Updated README progress to 42 / 49 required printed parts.

What I learned:

- Both middle body panels are now printed, so the main body shell is close to the final printed pieces.

Problems:

- Final fit with the body back, battery lid, trunk pieces, hardware, servos, and electronics is still pending.

Next:

- Print `body_back.stl` x1, then continue with `battery_pack_lid.stl`.

## 2026-08-18 - Body Back Panel Printed

Status: Body back panel printed.

What changed:

- Printed `body_back.stl` x1.
- Added the body back photo to `photos/printing/body/`.
- Marked the body back panel complete in the printing progress tracker.
- Updated README progress to 43 / 49 required printed parts.

What I learned:

- The main body shell print group is almost complete.

Problems:

- Final fit with the battery lid, trunk pieces, hardware, servos, and electronics is still pending.

Next:

- Battery pack lid completed later on 2026-08-18; continue with the remaining accessory prints.

## 2026-08-18 - Battery Pack Lid Printed

Status: Battery pack lid printed.

What changed:

- Printed `battery_pack_lid.stl` x1.
- Added the battery pack lid photo to `photos/printing/body/`.
- Marked the battery pack lid complete in the printing progress tracker.
- Updated README progress to 44 / 49 required printed parts.

What I learned:

- The required body print group is now complete.

Problems:

- Final fit with the body shell, trunk pieces, hardware, servos, battery holder, and power wiring is still pending.

Next:

- Accessory prints completed later on 2026-08-18; print the optional TPU foot bottoms next.

## 2026-08-18 - Accessory Prints Completed

Status: Remaining required accessory prints completed.

What changed:

- Printed `bulb.stl` x1.
- Printed `flash_light_module.stl` x1.
- Printed `flash_reflector_interface.stl` x1.
- Printed `speaker_interface.stl` x1.
- Printed `speaker_stand.stl` x1.
- Added accessory photos to `photos/printing/accessories/`.
- Marked all required accessory prints complete in the printing progress tracker.
- Updated README progress to 49 / 49 required printed parts.

What I learned:

- The required STL print checklist is complete.
- Only the optional TPU foot bottoms remain from the print guide.

Problems:

- Final fit with hardware, electronics, speaker parts, flash parts, and TPU foot bottoms is still pending.

Next:

- Print `foot_bottom_tpu.stl` x2 in TPU at 40% infill.
- Begin final fit checks while the robot-specific hardware arrives.

## Entry Template

```markdown
## YYYY-MM-DD - Short Title

Status:

What changed:

-

What I learned:

-

Problems:

-

Next:

-
```
