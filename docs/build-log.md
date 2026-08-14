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
