# Google Veo and Flow Example Prompt Reference

## Source and Scope


Scope mapping:

| Scope area | Coverage in this document |
|---|---|
| 1. Tool selection and limitations | Google Veo prompt structure, duration/session assumptions, and continuity constraints |
| 2. User constraints and objectives | Example intent, premise, style, and negative requirements |
| 3. Prompt script generation | Structured scene prompts and timestamped actions |
| 4. User review and approval | Review checkpoints, continuity checks, and approved prompt format |
| 8. Soundtrack generation | Replacement music and natural-sound prompt for the final video |

## 1. Google Veo Prompting Guidelines

Google Veo performs more predictably when the request is a directed shot description rather than a general premise.

### Recommended prompt structure

```text
[Cinematography]
[Subject]
[Action]
[Context]
[Style & Ambiance]
[Audio]
```

Optionally, use timestamp ranges for a multi-stage action within one clip:

```text
[00:00-00:03] ...
[00:03-00:08] ...
```

### Prompt fields

| Field | Purpose |
|---|---|
| Cinematography | Shot type, camera position, lens, focus, movement, and transitions |
| Subject | Main subject, appearance, clothing, texture, age, and identifying details |
| Action | Continuous movement, pacing, micro-actions, and shot timing |
| Context | Setting, environment, era, weather, background, and atmosphere |
| Style & Ambiance | Visual medium, lighting, color palette, mood, and realism level |
| Audio | Dialogue, sound effects, ambience, music, and exclusions |

### Prompting rules

- Be specific about camera angle, lens, and movement.
- Describe the physical subject and its identifying features.
- Describe continuous actions and their pacing rather than a general goal.
- Use timestamp ranges for several actions within one generation.
- Prefer positive descriptions: say what should appear instead of only stating what should be absent.
- When a negative-prompt field exists, use concise raw terms such as `blur`, `watermark`, `text`, `subtitles`, or `crowds`.
- Explicitly identify desired dialogue and sound effects.
- State `no background music` or `no subtitles` when those elements are not wanted.
- Preserve the same character, clothing, lighting, color grade, and setting across scenes.
- Use an end frame or reference image when the selected interface supports continuity control.

## 2. Plain-English Prompt versus Structured Prompt

### Example premise

> A tired detective sitting in his office at night drinking coffee while it rains outside.

### Structured Veo prompt

```text
[Cinematography]: Medium shot at eye level, transitioning into a slow, smooth dolly-in toward the subject. Shot on a 50mm lens with shallow depth of field, keeping the background softly out of focus.

[Subject]: A weathered detective in his late 40s with salt-and-pepper stubble, dark circles under his eyes, wearing a rumpled white dress shirt with rolled-up sleeves and a loosened dark tie.

[Action]: He sits hunched over a cluttered wooden desk, slowly lifting a chipped ceramic mug to take a sip of coffee. Hot steam curls upward as his eyes scan a spread of black-and-white crime-scene photographs.

[Context]: A dimly lit 1940s noir-style precinct office at night. Rain streaks a window behind him; Venetian blinds, a brass desk lamp, and an overflowing ashtray complete the room.

[Style & Ambiance]: Cinematic photorealism on grainy 35mm film. Warm tungsten light illuminates the left side of his face, while cool blue neon flickers through the blinds. Muted shadows, amber, and slate blue.

[Audio]: Heavy rain on the window, distant thunder, and the subtle clink of the mug on the wooden desk. No background music, no subtitles.
```

## 3. Example Video Premise

### Original user premise

> A white unicorn runs through a dense jungle on a mountain and reaches a cliff. It jumps, sprouts wings, flies upward, and glides toward a lake. It lands beside a female unicorn and two foals. The family feeds on strawberry plants while a pink crocodile quietly approaches the shore. The unicorns detect it and fly away. The crocodile returns to the lake and is greeted by three baby crocodiles.

### Expanded production intent

- Visual style: High-budget fantasy cinema, photorealistic 35mm film.
- Main subjects: One white adult male or winged unicorn; one adult female unicorn; two foals; one giant pink crocodile; baby crocodiles.
- Pacing: Adventure, flight, peaceful reunion, suspense, escape, and warm resolution.
- Lighting: Golden-hour jungle and lake scenes transitioning from sunset to dusk.
- Audio: Natural ambience synchronized with action, an original orchestral score, no dialogue, and no subtitles.
- Continuity: Character appearance, wing shape, horn, coat, lighting, and color grading remain consistent between scenes.
- Frame and reference control: Use generated end frames or approved source frames before subsequent sessions.

## 4. Example 19-Scene Prompt Script

The following structure is suitable for repeated short generations and is consistent with the MAD workflow's session, segment, verification, and human-review stages.

### Scene 1 — Jungle sprint

- **Cinematography:** Low-angle hoof-level tracking shot, rising to medium-wide profile; 35mm anamorphic lens; shallow depth of field.
- **Subject:** Pure-white muscular unicorn with pearlescent horn, silver-white mane and tail.
- **Action:** Gallop uphill through undergrowth, leap over a fallen log, weave through vines, and approach the bright forest edge.
- **Context:** Dense tropical mountain jungle with mist, banyan roots, ferns, wet soil, and distant summit light.
- **Style:** Photorealistic fantasy, golden sunbeams, deep greens, amber highlights.
- **Audio:** Hoofbeats, snapping twigs, rushing leaves, jungle birds, wind, and rising strings.
- **Verification criteria:** One white unicorn; no extra characters; uphill jungle sprint; correct leap; no text or subtitles.

### Scene 2 — Leap from the cliff

- **Cinematography:** Low-angle side tracking shot, sweeping crane plunge, then upward tilt.
- **Action:** Gallop onto the rock cliff, launch over the edge, unfold large white-feathered wings, and beat upward.
- **Continuity:** Preserve the unicorn's exact coat, horn, mane, mud marks, scale, and golden-hour grade from Scene 1.
- **Verification criteria:** One cliff exit; visible wing emergence; no failed, reversed, or duplicated animation; no text or subtitles.

### Scene 3 — Climb higher

- **Cinematography:** Smooth aerial side and three-quarter tracking shot; stabilized gimbal; deep focus.
- **Action:** Perform slow, powerful wing downstrokes; fold all legs close under the torso; climb through thin clouds.
- **Style:** Gold and blue high-altitude sky with visible mountain valleys below.
- **Verification criteria:** Legs do not gallop or run while airborne; continuous wingbeat; preserved identity and wing appearance.

### Scene 4 — Effortless glide

- **Cinematography:** Elevated side-three-quarter track drifting close to a medium-wide profile.
- **Action:** Stop flapping and glide on thermal currents; make only subtle wingtip corrections.
- **Continuity:** Preserve the same white winged unicorn and all legs in a tucked, motionless position.
- **Verification criteria:** No extra flight movement, leg movement, or character replacement.

### Scene 5 — Flight through clouds

- **Cinematography:** Wide profile arcing forward into a three-quarter front angle.
- **Action:** Bank gently through dense clouds and trail cloud vapor from the wingtips.
- **Style:** Warm sunlight through cloud gaps with rich atmospheric haze.
- **Audio:** High-altitude wind and soft feather ruffles; no hoofbeats or ground sounds.

### Scene 6 — Continued cloud flight

- **Cinematography:** Wide profile and smooth forward arc.
- **Action:** Continue gliding through cloud banks with frozen legs and subtle wing adjustments.
- **Continuity:** Match the appearance, lighting, speed, and scale established in Scenes 3–5.
- **Verification criteria:** No reset to climbing or galloping motion unless specifically approved.

### Scene 7 — Begin descent

- **Cinematography:** Elevated side-three-quarter tracking shot moving behind and above the subject.
- **Action:** Tilt the wings slightly downward and begin a controlled descent through thinning clouds.
- **Context:** A distant lake appears among green hills and forested valleys.
- **Verification criteria:** Descent direction remains clear; lake enters from the correct horizon; no abrupt posture change.

### Scene 8 — Approach the lake and family

- **Cinematography:** Over-the-wing aerial tracking shot, descending and tilting forward.
- **Action:** Continue toward the lake while faint silhouettes of a female unicorn and foal appear near the shore.
- **Continuity:** The reunion figures must match subsequent scenes.
- **Verification criteria:** No more than the two expected distant family figures visible unless an approved shot change is provided.

### Scene 9 — Landing and reunion

- **Cinematography:** Aerial track descending to eye level, slowing into medium-wide landing coverage.
- **Action:** Fold the legs, brake with the wings, and land softly. Fold the wings. The two foals and female unicorn welcome the returning adult.
- **Subject:** Exactly one returned winged adult, one wingless adult female, and two foals.
- **Verification criteria:** Soft landing; correct family count; foals remain baby-sized; no additional unicorn appears.

### Scene 10 — Family feeds on strawberries

- **Cinematography:** Eye-level medium-wide shot with a slight right pan.
- **Action:** The female joins the family, then all four feed in the foreground strawberry patch.
- **Continuity:** Use the exact lake, meadow, lighting, strawberry patch, wing position, and family identity.
- **Verification criteria:** Exactly four unicorns, all pure white, all wing states consistent with the approved state, no additional unicorn.

### Scene 11 — Peaceful aerial pullback

- **Cinematography:** Eye-level crane-up and pullback to a wide lakeside aerial view.
- **Action:** Continue grazing and occasionally lift heads toward the lake while the sun sets.
- **Verification criteria:** Exactly four unicorns and no newly introduced subjects.

### Scene 12 — Crocodile enters unseen

- **Cinematography:** Low-angle water-level tracking shot behind the predator.
- **Subject:** One giant pink crocodile with golden eyes and a submerged pink snout.
- **Action:** Move forward an inch at a time toward the shore, leaving tiny ripples.
- **Continuity:** Keep the unicorn family distant and unaware.
- **Verification criteria:** Predator remains subtle; no crocodile body inconsistency; no unicorn reaction yet.

### Scene 13 — Crocodile approaches

- **Cinematography:** Water-level shot immediately behind and beside the crocodile.
- **Action:** Cut a silent V-shaped wake toward the shoreline.
- **Context:** The four grazing unicorns are closer and remain distracted.
- **Verification criteria:** No splash; no facial or scale mismatch; clear continuous approach direction.

### Scene 14 — Unicorn detects danger

- **Cinematography:** Eye-level medium-wide shot, moving to a tense push-in on the lead adult.
- **Action:** Four previously wingless unicorns stop grazing. The lead raises its head, snorts, and watches the lake. The female shields the foals.
- **Continuity:** Match the exact framed strawberry patch and remove all visible wings unless the current continuity design intentionally shows the previously landing winged unicorn.
- **Human review point:** Confirm family identity and wing state before approving the next chase scene.

### Scene 15 — Chase from the lake

- **Cinematography:** Wide-angle dynamic lateral shoreline tracking shot.
- **Action:** The pink crocodile emerges and charges. The four unicorns gallop uphill while shielding the foals.
- **Audio:** Water splash, crocodile claws, hoofbeats, alarmed snorts, urgent percussion, and strings.
- **Verification criteria:** Correct number of unicorns; crocodile fully emerged; no visual discontinuity at the shoreline.

### Scene 16 — Unicorns sprout wings and escape

- **Cinematography:** Dynamic tracking shot transitioning to a low-angle upward tilt.
- **Action:** All four unicorns simultaneously sprout proportionate wings and rise while the crocodile skids to a halt below.
- **Subject:** Two adult winged unicorns and two winged foals.
- **Verification criteria:** Proportions, simultaneous wing emergence, no duplicated wings or subjects, correct crocodile reaction.

### Scene 17 — Family flies away

- **Cinematography:** Sweeping aerial tracking shot followed by a wide panoramic view.
- **Action:** Form a protective V formation, climb, synchronize wingbeats, and transition into a peaceful glide.
- **Verification criteria:** Exactly four winged unicorns; adults flank foals; legs remain tucked; flight remains continuous.

### Scene 18 — Crocodile returns to the lake

- **Cinematography:** Low-angle tracking at eye level, ending at water level.
- **Action:** The crocodile lowers its gaze, turns toward the lake, walks down the bank, and submerges.
- **Subject:** Giant pink crocodile only; no unicorns visible.
- **Tone:** Reflective, disappointed, and calm.
- **Verification criteria:** No remaining unicorn; smooth turn; scale and color remain consistent.

### Scene 19 — Reunion with baby crocodiles

- **Cinematography:** Low-angle water-level medium-wide shot.
- **Subject:** One giant pink crocodile and two baby crocodiles with matching pastel-pink scales.
- **Action:** The babies paddle over, nuzzle the adult, and one offers a small silver fish.
- **Tone:** Peaceful, affectionate, and warm at dusk.
- **Verification criteria:** Exactly three crocodiles; babies are clearly smaller; no extra adult crocodiles; fish remains in one baby's mouth.

## 5. Continuity and Reference Strategy

Before generating a session after a provider quota or limit is reached:

1. Capture the approved end frame from the last successful clip.
2. Record the frame number, timestamp, and visual state.
3. Record the next scene, expected motion delta, and camera transition.
4. Include the end frame as a reference image when supported.
5. Repeat critical subject attributes in the next prompt.
6. Add a positive continuity instruction:

```text
Continue exactly from the supplied reference frame. Preserve the subject's identity, scale,
coat, horn, mane, wing shape, clothing or adornments, time of day, lighting direction,
color grade, scene geometry, and camera distance. Animate only the actions specified below.
```

7. Add an acceptance criterion for each continuation step.
8. Flag identity, pose, lighting, or framing changes for human review.

## 6. Recommended Segment Record

```json
{
  "segment_id": "SCENE-09",
  "session_id": "SESSION-03",
  "duration_seconds": 8,
  "reference_frame": "scene-08-end-frame.png",
  "prompt": "",
  "negative_prompt": ["text", "subtitles", "watermark", "extra unicorn"],
  "continuity_requirements": [],
  "acceptance_criteria": [],
  "verification_status": "pending",
  "human_decision": null
}
```

## 7. Optional Soundtrack Example

### User request

> Replace the existing soundtrack. The instrumentation and natural sounds should match the scenery and action.

### Structured replacement-audio prompt

#### 0:00–0:14 — Forest sprint

> Upbeat adventurous fantasy orchestral music with lively pizzicato strings and light bodhran percussion. Add natural hoofbeats on dirt and roots, rustling ferns, chirping forest birds, snapping twigs, and a sudden dramatic whoosh at the cliff edge.

#### 0:14–1:12 — Soaring above the clouds

> Majestic uplifting cinematic score with sweeping string sections, noble French horns, and sparkling harp arpeggios. Blend in crisp high-altitude wind, rhythmic feathered wingbeats, and a light ethereal atmosphere.

#### 1:12–1:59 — Lakeside peace and hidden danger

> Begin with peaceful pastoral fantasy featuring a wooden flute, soft acoustic guitar, gentle breeze, calm lake ambience, and distant birds. Crossfade gradually into low pulsing cellos, murky water ripples, and tense suspense with quiet silences.

#### 1:59–2:29 — Ambush and magical escape

> High-stakes action score with timpani, urgent staccato strings, and a triumphant brass fanfare. Synchronize crashing lake water, scrambling footsteps, crocodile movement, unicorn galloping, and a magical shimmering chime as wings unfold.

#### 2:29–3:00 — Dusk by the water

> Gentle emotional orchestral outro led by a warm cello and delicate felt piano. Include soft water wading and lapping, twilight marsh ambience, distant insects, and tender baby-crocodile chirps.

### Soundtrack acceptance criteria

- Instrumentation matches each scene's emotional tone.
- Natural sounds match visible actions and scene geography.
- Music crossfades align with scene transitions.
- No dialogue or unintended singing is generated.
- Finale volume allows natural ambience to remain audible.
- User approves the prompt before audio generation.
- The final mixed MP4 receives both LLM and human review.

## 8. Review Points

The example flow requires review at the following checkpoints:

1. **Tool profile review:** Confirm quota, duration, and reference-frame support.
2. **Premise review:** Confirm story, objective, visual style, and negative constraints.
3. **Prompt-script review:** Confirm all 19 scenes and continuity instructions.
4. **Segment review:** Inspect flagged scenes or every scene if configured.
5. **Human override review:** Approve, retry, reject, or carry forward with comments.
6. **Combined-video review:** Check scene order, transitions, continuity, pacing, and duration.
7. **Music-prompt review:** Confirm soundtrack structure and natural sound requirements.
8. **Final-media review:** Check synchronized music and natural sound after attachment.

## 9. Relationship to the MAD Scope

This example demonstrates scope items:

- **Scope 1:** Google/Veo limitations are translated into a prompt format and generation profile.
- **Scope 2:** The unicorn story is expressed as structured requirements.
- **Scope 3:** Prompt scripts preserve continuity across scene boundaries and sessions.
- **Scope 4:** The scene prompts are suitable for user editing and approval before generation.
- **Scope 5–7:** The 19 scenes are suitable for segment generation, verification, human decisions, and concatenation.
- **Scope 8–12:** The sample soundtrack prompt supports user review, music generation, media attachment, and final review.
