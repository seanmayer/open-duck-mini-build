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

## 2026-08-18 - TPU Foot Bottoms Printed

Status: Optional TPU foot bottoms printed.

What changed:

- Printed `foot_bottom_tpu.stl` x2.
- Added the TPU foot bottom photo to `photos/printing/feet/`.
- Marked the optional TPU foot bottoms complete in the printing progress tracker.
- Updated README progress to show the full printing phase complete, including the TPU feet.

What I learned:

- TPU is much harder to remove from the print plate than PLA.
- A release layer, such as glue stick or Bambu liquid glue, should help on future TPU prints.

Problems:

- TPU had very strong bed adhesion, so the parts should be inspected before final foot assembly.

Next:

- Fit the TPU bottoms to the PLA feet.
- Begin final fit checks and hardware preparation while electronics and servos arrive.

## 2026-08-19 - Foot Micro Switches Arrived

Status: Foot contact switches received.

What changed:

- Received 4 x SS-10 style micro switches with pin plungers.
- Added the switch photo to `photos/hardware/`.
- Added a hardware sourcing tracker for robot-specific parts.
- Updated README hardware sourcing progress.

What I learned:

- These switches are SPDT, so the terminals should be checked before wiring to identify common, normally open, and normally closed.
- The printed feet can now be checked against the actual switch bodies and plunger travel.

Problems:

- Final fit in the foot assemblies is still pending.
- Switch wiring is not started yet.

Next:

- Test-fit the switches in the foot assemblies.
- Use a multimeter continuity check to identify the switch terminals before soldering.
- Continue tracking incoming servos and electronics as they arrive.

## 2026-08-19 - Battery Order Arrived

Status: First power hardware received.

What changed:

- Received the Nitecore Intellicharger NEW i2 battery charger.
- Received 2 x P30B 18650 Li-ion cells.
- Added battery order photos to `photos/hardware/`.
- Updated the hardware sourcing tracker with the received charger and cells.
- Updated README hardware sourcing progress.

What I learned:

- Battery sourcing has started, but the charger and cells are only part of the power system.
- The robot still needs a confirmed in-robot power path before the batteries are connected.

Problems:

- BMS/protection, regulator, battery holder, switch, and power wiring still need to be confirmed.

Next:

- Check each cell voltage with a multimeter.
- Store the cells safely until assembly.
- Do not wire the cells into the robot until the BMS/protection, regulator, switch, and wiring plan are confirmed.

## 2026-08-21 - Second Hardware Batch Arrived

Status: Motion, mechanical, wiring, and additional power parts received.

What changed:

- Received a multi-pack of SG90 9g micro servos with horns and mounting hardware.
- Received 20 x 8 x 22 x 7 mm bearings.
- Received 2 x 2S 18650 battery holders with leads.
- Received a 2-7S-input UBEC rated for a regulated 5V 5A output.
- Received 12 pairs of XT30 connectors with heat-shrink tubing.
- Received a kit of DC barrel plug/socket screw-terminal adapters.
- Received red and black power wire.
- Received 5 ml of Loctite 243 medium-strength threadlocker.
- Added all eight arrival photos to `photos/hardware/` and updated the sourcing tracker, workshop checklist, roadmap, and README.

What I learned:

- The smaller motion hardware and several mechanical and wiring items are now available for fit checks and bench testing.
- The new UBEC can provide a 5V rail, but it does not replace the battery BMS/protection or main power switch.
- The battery holders are passive components and must not be treated as battery protection.

Problems:

- The BMS/protection and main power switch are still outstanding, so the 18650 cells must remain disconnected from the robot.
- The wire gauge, DC barrel dimensions, connector polarities, bearing fit, and servo operation still need to be verified.

Next:

- Test-fit and bench-test the SG90 servos and bearings.
- Verify the UBEC output, battery-holder wiring, wire gauge, and connector polarity with a multimeter before making power leads.
- Keep the cells out of the holders until the protected, switched power path is fully confirmed.

## 2026-08-23 - Power Protection And Raspberry Pi Support Parts Arrived

Status: Additional power-protection and bench-setup parts received.

What changed:

- Received four 2S BMS/protection boards marked for 4.2V / 8.4V packs and labelled 20A.
- Received a UK mains DC barrel power adapter.
- Received a 4K/UHD HDMI cable for Raspberry Pi display/setup work.
- Received a GeekPi 13-piece 40-pin GPIO header kit.
- Added arrival photos and updated the hardware tracker, roadmap, and README.

What I learned:

- The BMS boards are physically available, but their printed rating is not enough to establish safe use in this robot; their wiring, protection functions, and continuous-current capability must still be checked.
- The GPIO kit gives options for the future Raspberry Pi, but does not replace the still-outstanding Pi itself.

Problems:

- The DC adapter label is not visible in the arrival photo, so its output voltage, polarity, connector size, and current rating are unconfirmed.
- The main battery power switch is still outstanding.

Next:

- Confirm the BMS terminal mapping and suitability for the planned 2S battery pack before connecting cells.
- Measure the DC adapter output and polarity with a multimeter before connecting it to electronics.
- Keep the cells disconnected until the protected, switched power path is fully confirmed.

## 2026-08-24 - Rear-Panel Battery Holder Fit Check

Status: Replacement holder ordered; no battery cells installed and no power wiring started.

What changed:

- Test-fitted the original 2S holder against the printed rear battery panel.
- Found that its outer casing does not fit the intended mounting area.
- Ordered a compact replacement 2S holder rather than spending additional time and filament on a custom printed holder.
- Kept the separate 2S BMS/protection board as the planned pack-protection component.

What I learned:

- The rear panel needs a compact holder; mechanical fit needs to be checked before any cells or wiring are added.
- A holder supplies the physical cell contacts, while the separate BMS still needs the pack negative, cell midpoint, and pack positive connections.

Problems:

- The replacement holder has not arrived, so its exact fit, contacts, and access to the BMS midpoint remain unverified.
- The main power switch and final protected wiring plan are still outstanding.

Next:

- Measure and test-fit the replacement holder on arrival with no cells installed.
- Confirm its 2S series arrangement and BMS connection points before soldering.
- Keep the cells disconnected until the complete protected and switched power path is verified.

## 2026-08-24 - Main Servo Delivery Checked

Status: Received and visually counted; installation and power-on testing have not started.

What changed:

- Received 14 Feetech STS3215 serial bus servos marked 7.4V and 1:345.
- Confirmed that each servo arrived with its cable, horn/disc, mounting screws, and centre screw.

Next:

- Keep every servo's accessories together and label the units before assembly.
- Begin mechanical dry fitting into the printed body, limbs, and head parts.
- Do not permanently install horns/discs or power the servos until they can be centred with the final controller and verified power setup.

## 2026-08-25 - IMU Delivery Checked

Status: Received; not mounted or wired.

What changed:

- Received the BNO055 IMU breakout with loose header pins.

Next:

- Confirm the required orientation, pinout, and I2C wiring before mounting it.
- Leave the header pins unsoldered until the mounting and wiring approach is confirmed.

## 2026-08-25 - Main Power Switch Delivery Checked

Status: Received; not installed or wired.

What changed:

- Received the panel-mount ON/OFF main power switch with its supplied leads and crimp connectors.

Next:

- Confirm the switch terminals, current rating, mounting fit, and wire polarity with a multimeter before installation.
- Keep the cells disconnected until the BMS and complete protected, switched power path are verified.

## 2026-08-26 - Compact Battery Holder Fitted to Replacement Rear Panel

Status: Holder received and mechanically fit-checked; no cells installed and no power wiring started.

What changed:

- Received the compact replacement 2S 18650 battery holder and confirmed that it fits the rear-panel mounting area.
- Reprinted the rear/body back panel after the earlier panel broke during an attempted fit of the oversized original holder.
- Recorded that the earlier panel had a weak section where the print changed from one PLA filament to another; the oversized holder applied the force, but the filament-change weakness was the reason the panel failed.

What I learned:

- Test-fit bought components before committing to wiring or final assembly.
- Avoid changing PLA filament partway through a structurally important print where possible, especially around stressed mounting features.

Next:

- Secure the holder in the replacement rear panel and inspect the contacts and lead routing with no cells installed.
- Verify the holder's 2S series arrangement and the BMS sense-wire connection points before soldering or installing cells.
- Keep the cells disconnected until the complete protected, switched power path is verified.

## 2026-08-29 - 2S Power Pack Wiring Completed

Status: Power-pack subassembly completed and end-to-end switched output verified.

What changed:

- Assembled the 2S 18650 battery pack in the compact holder.
- Connected the battery holder to the 2S 20A BMS.
- Added the cell midpoint connection to the BMS.
- Mounted the BMS inside the printed battery enclosure.
- Installed and wired the rocker power switch.
- Wired the USB-C charging board using its BAT and GND pads.
- Connected the 5V / 5A UBEC.
- Created 7.4V power branches for the UBEC and the future motor-controller supply.
- Completed the main power-pack wiring.
- Added completion photo: [power-pack-complete-2026-08-29.jpg](../photos/hardware/power-pack-complete-2026-08-29.jpg).

Wiring recorded:

- Battery negative -> BMS 0V.
- Cell midpoint -> BMS 4.2V.
- Battery positive -> BMS 8.4V.
- BMS P+ -> positive 7.4V rail.
- BMS P- -> rocker switch -> negative 7.4V rail.
- 7.4V rails branch to the UBEC and motor-controller supply.
- UBEC converts the battery supply to regulated 5V.
- USB-C charging board is wired using BAT and GND.

Testing:

- Confirmed each 18650 cell measured approximately 3.5V.
- Confirmed total series voltage measured approximately 7V.
- Confirmed the BMS midpoint measured approximately one-cell voltage.
- Tested rocker switch using multimeter continuity mode.
- Switch ON -> continuity.
- Switch OFF -> open circuit.
- UBEC output with switch ON -> approximately 5V.
- UBEC output with switch OFF -> 0V.
- End-to-end switched power operation successfully verified.

Challenges:

- Identifying the correct BMS battery and output connections.
- Understanding why a 2S BMS requires a midpoint connection.
- Finding the physical midpoint of the two series-connected cells.
- Learning how the positive and negative power rails branch to multiple loads.
- Learning how to make 1-to-2/Y wire splices.
- Improving wire stripping, tinning, and soldering technique.
- Determining the correct USB-C charger solder pads.
- Getting reliable multimeter probe contact on small solder joints.
- Encountered misleading BMS output voltage readings while probing.
- Battery-holder contact briefly caused the pack to appear as approximately one-cell voltage until the cell was reseated.

What I learned:

- A 2S battery is two cells connected in series.
- The BMS monitors the individual cells using the midpoint connection.
- BMS voltage labels represent the corresponding node voltages at full charge.
- The BMS provides battery protection rather than voltage regulation.
- The UBEC converts the variable 2S battery voltage into a stable 5V supply.
- The UBEC and motor controller are powered in parallel from the 7.4V rails.
- The rocker switch interrupts the negative power path.
- Pre-tinning stranded wires can make PCB soldering easier.
- Soldered Y-splices can create simple power-distribution branches.
- Functional end-to-end voltage testing is useful alongside individual connection testing.

Safety:

- Removed both 18650 cells before soldering.
- Avoided soldering directly to the 18650 cells.
- Checked polarity before connecting components.
- Used the multimeter to verify voltages before progressing.
- Avoided bridging adjacent BMS pads with multimeter probes.
- Continue removing the batteries when the unfinished robot is not being worked on.

Current status:

- Power-pack assembly complete.
- Battery series configuration verified.
- BMS wiring complete.
- Power switch working.
- USB-C charger board wired.
- UBEC connected and producing the expected 5V.
- Switched 5V output successfully tested.
- Raw 7.4V branch prepared for the motor electronics.

Next:

- Verify USB-C charging operation in a controlled test.
- Continue assembly of the RoboDuck Mini electronics.
- Connect the 7.4V supply to the motor-control system when ready.
- Connect the regulated 5V supply to the appropriate electronics.
- Continue checking polarity and voltage before connecting each new subsystem.

## 2026-09-06 - Servo Controller Bench Setup Planned

Status: Next electronics step planned; not wired or tested yet.

What changed:

- Confirmed that the Waveshare serial bus servo driver boards are the intended interface for the STS3215 serial bus servos.
- Recorded that two controller boards are enough for the 14 servos because the STS3215 servos share a serial bus and each servo is addressed by its own ID.
- Chose a laptop-first approach for initial servo ID programming, rather than starting on the Raspberry Pi, to keep the Pi setup clean and make driver/software testing easier.
- Confirmed that the UBEC's servo-style output connector is the regulated 5V output and is not the correct power feed for the STS3215 servo motor rail.

Planned wiring:

- Splice a new red/black branch from the switched 7.4V output rail between the BMS/power switch and the UBEC input.
- Feed this switched 7.4V branch into the Waveshare controller power input, preferably using the green screw terminal for the first bench test.
- Keep the UBEC branch separate: the UBEC remains for regulated 5V electronics power, not STS3215 servo power.
- Connect the Waveshare controller to the laptop over USB for data/control.
- Connect one STS3215 servo to the controller for the first ID check/programming test.

Safety checks before connecting a servo:

- Remove the 18650 cells while making the splice or changing power wiring.
- With no servo connected, switch the pack on and measure at the Waveshare controller input.
- Confirm the red wire is positive and the black wire is negative.
- Confirm the controller input reads approximately the current 2S pack voltage, expected around 7.0-8.4V depending on cell charge.
- Switch the pack off and confirm the controller input drops to 0V.
- Only connect one servo after the input voltage and polarity are confirmed.

Next:

- Make the switched 7.4V branch for the Waveshare controller.
- Bench-test the controller with one STS3215 servo from the laptop.
- Read or assign the first servo ID.
- Label each servo physically before moving to the next one.
- Build a servo ID map before final mechanical installation.

## 2026-09-14 - Servo Controller Power Wires Prepared

Status: Wiring preparation started; no soldering or power-on test performed yet.

What changed:

- Started the next electronics step after the completed power pack.
- Prepared the red/black wires for the Waveshare serial bus servo driver board power connection.
- The planned connection remains a switched 7.4V branch from the power-pack output rail before the UBEC input.
- Soldering the branch into the power-pack wiring is planned for the next work session.

Notes:

- Progress was limited today because last week was spent hacking the media wall lights.
- This is preparation only: the Waveshare controller has not yet been connected to the 7.4V rail.
- The UBEC 5V output remains separate and should not be used for STS3215 servo motor power.

Next:

- Remove the 18650 cells before soldering the new branch.
- Solder the red/black branch into the switched 7.4V output rail between the BMS/power switch and the UBEC input.
- Connect the new branch to the Waveshare controller power input.
- With no servo connected, use the multimeter to confirm polarity and approximately 7.0-8.4V at the controller input.
- After the voltage check passes, connect one STS3215 servo and use the laptop over USB for the first ID check/programming test.

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
