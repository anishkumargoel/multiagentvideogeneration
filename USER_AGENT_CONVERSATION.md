# Original Google Veo and Flow User-Agent Conversation

Related documents:

- [`VIDEO_GENERATION_WORKFLOW_MAD.md`](./VIDEO_GENERATION_WORKFLOW.md) — overall workflow scope.
- [`GOOGLE_VEO_AND_FLOW_REFERENCE.md`](./GOOGLE_VEO_AND_FLOW_REFERENCE.md) — reformatted reusable reference.



# Covers scope points 1 and 2 

**USER PROMPT**
Provide a an example details and  structured prompt to use the google flow video/ Veo generation service. 

**AGENT RESPONSE**
Google’s video generation model (Veo) responds best when you stop describing a scene casually and start directing it like a cinematographer. Plain English descriptions often leave the camera angle, lighting, pacing, and audio up to the model's defaults, which is why finer details get lost.

​Google recommends a structured 5-part core formula (plus audio and timestamping for newer Veo versions):

​[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance] + [Audio]

​1. The Structured Prompt Template
​You can copy and fill in this labeled template. Using explicit labels helps the model separate camera behavior from visual details and sound.



[Cinematography]: Shot type (e.g., Medium close-up, wide establishing shot), camera movement (e.g., slow dolly-in, tracking shot, static), angle (e.g., low-angle), and lens/focus (e.g., 35mm lens, shallow depth of field, soft bokeh).

[Subject]: Detailed physical description of the main focus—age, clothing textures, facial expression, materials, or colors.

[Action]: Specific, continuous movement happening during the clip, including micro-actions (e.g., fingers tapping, steam rising, fabric fluttering) and pacing (e.g., slow-motion, real-time).

[Context]: The immediate environment, background elements, era, and weather/atmospheric details.

[Style & Ambiance]: Visual medium (e.g., photorealistic 35mm film, 3D Pixar-style animation, 1980s VHS), lighting setup (e.g., warm golden hour backlight, harsh neon rim lighting), and color palette.

[Audio]: Spoken dialogue in quotes, specific sound effects (SFX), ambient background noise, and music cues (or "no background music").

2. Concrete Example: Plain English vs. Structured Prompt
​Plain English (What usually misses details):

​"A tired detective sitting in his office at night drinking coffee while it rains outside."


​Structured Veo Prompt (High-control):

​[Cinematography]: Medium shot at eye level, transitioning into a slow, smooth dolly-in toward the subject. Shot on a 50mm lens with a shallow depth of field, keeping the background softly out of focus.

[Subject]: A weathered detective in his late 40s with salt-and-pepper stubble, dark circles under his eyes, wearing a rumpled white dress shirt with rolled-up sleeves and a loosened dark tie.

[Action]: He sits hunched over a cluttered wooden desk, slowly lifting a chipped ceramic mug to take a sip of coffee. Wisps of hot steam curl upward from the mug as his eyes scan a spread of black-and-white crime scene photographs.

[Context]: A dimly lit, 1940s noir-style precinct office at night. Venetian blinds cover a rain-streaked window behind him, with a brass desk lamp and overflowing ashtray on the table.

[Style & Ambiance]: Cinematic photorealism on grainy 35mm film. Chiaroscuro lighting: warm tungsten light from the desk lamp illuminates the left side of his face, while cool blue neon light from a street sign outside flickers through the blinds. Muted color palette of deep shadows, amber, and slate blue.

[Audio]: Ambient noise of heavy rain pattering against the windowpane and a distant, low rumble of thunder. SFX: The subtle clink of the ceramic mug being set back down on the wooden desk. No background music, no subtitles.



​3. Advanced Control Techniques for Veo
​Timestamp Prompting (Multi-Shot Pacing): If you want a specific sequence of events within a single generation, break the action into timed intervals:
​[00:00-00:03] Extreme close-up of a wristwatch ticking, shallow depth of field.
​[00:03-00:06] Whip pan up to a woman standing on a crowded train platform, looking anxiously down the tracks.
​Use Positive Descriptions Instead of Negatives: Avoid writing "no walls" or "don't show crowds" in the main prompt. Instead, describe what is there (e.g., "an empty, deserted street"). If your interface has a dedicated Negative Prompt field, list only raw nouns you want excluded (e.g., blur, watermark, text, subtitles, crowds).

​Explicitly Anchor Audio & Subtitles: Because newer Veo models generate synchronized audio, leaving audio blank often causes the model to invent unwanted background music. Always state "no background music" if you only want natural sound effects, and add "no subtitles" if you include spoken dialogue. 

# Covers scope points 3 to 4
**USER PROMPT**
Create structured prompt for - A white colored unicorn is running through a dense jungle. This jungle is on a mountain and ends at a cliff. The unicorn jumps from the cliff, sprounts wings and flies in the sky. the unicorn keeps flying higher and then keeeps gliding. the unicorn nearns as lake and gently lands near the edge of the lake next to his family. There are two foals and another female unicorn waiting for him. the much through strawebbery bushes. Unknown to them, a pink corocodile is lurking in the lake. It silently swims towards tha lake shore. the unicorns are alerted by the nosie and as soon as the croocodile emerges from the lake, they start running. They eventually sprot wings and glide into the sky. Dejected, the crocodile returns to the lake. Three baby crocodiles greet him.  

**AGENT RESPONSE**
**SCENE 1**
[Cinematography]: Dynamic low-angle tracking shot, moving rapidly alongside and slightly ahead of the subject at hoof level, then smoothly rising to a medium-wide profile shot. Shot on a 35mm anamorphic lens with shallow depth of field, slight handheld kinetic vibration to convey speed, and crisp focus locked on the subject while foreground ferns whip past in motion blur.

[Subject]: A majestic, pure-white unicorn with a muscular build, a pearlescent, spiraling ivory horn, and a long, silky silver-white mane and tail streaming backward in the wind. Flecks of mud and morning dew cling to its lower legs and fetlocks.

[Action]: The unicorn is galloping furiously uphill through thick undergrowth, leaping cleanly over a mossy fallen log and weaving between tangled vines. Its muscles ripple beneath its coat with each stride, nostrils flaring as it pushes forward toward higher ground, building momentum as the forest ahead begins to brighten.

[Context]: A lush, ancient tropical mountain jungle with a steep upward incline. Towering banyan and mahogany trees draped in hanging lianas, oversized emerald ferns, damp dark soil, and swirling ribbons of low-lying mountain mist. Ahead in the distance, the dense tree canopy begins to thin into bright, open sky, hinting at the summit without revealing the edge.

[Style & Ambiance]: High-budget fantasy cinema aesthetic, photorealistic, shot on 35mm film. Volumetric lighting with dramatic golden-hour sunbeams piercing diagonally through the dense canopy, illuminating floating dust motes, pollen, and kicked-up moisture. Rich color palette of deep jungle greens, earthy browns, luminous ivory, and warm amber highlights.

[Audio]: Heavy, rhythmic thudding of hooves against damp earth and snapping twigs, accompanied by the rustling of dense leaves brushing past the unicorn's body and its steady, forceful breathing. Ambient sounds of distant exotic jungle birds and wind rushing through high mountain trees. Subtle, swelling orchestral strings building tension at the end of the clip. No dialogue, no subtitles.

**SCENE 2**
[Cinematography]: Dynamic multi-stage aerial tracking shot. Starts as a low-angle side tracking shot matching the unicorn's sprint, transitions seamlessly into a sweeping crane shot that plunges off the cliff edge alongside the subject, and tilts upward into a wide, majestic upward angle as the unicorn ascends into the sky. Shot on a 35mm anamorphic lens, shifting from kinetic handheld energy to ultra-smooth aerial gimbal motion, crisp focus on the subject.

[Subject]: The same majestic, pure-white unicorn with a muscular build, a pearlescent, spiraling ivory horn, and a long, silky silver-white mane and tail streaming in the wind, with flecks of dark jungle mud still visible on its lower legs and fetlocks. During the leap, two massive, radiant white-feathered wings unfurl from its shoulders, glowing faintly with translucent gold-edged plumage.

[Action]: 
[00:00-00:02] The unicorn bursts violently out of the dense jungle treeline at full gallop, hooves tearing through the final ferns onto open rocky terrain at the sheer cliff edge. 
[00:02-00:04] Without breaking stride, it launches off the precipice into open air in a powerful, graceful arc, momentarily suspended in mid-air as its muscles tense. 
[00:04-00:08] Brilliant, shimmering white wings erupt and unfold dramatically from its back in a burst of golden light particles; the wings beat downward with immense power, catching the mountain updraft as the winged unicorn banks and soars upward into the open sky.

[Context]: The abrupt, dramatic edge of a towering mountain cliff where lush tropical jungle gives way to jagged mossy granite rocks. Beyond the sheer drop lies a breathtaking expanse of misty mountain peaks, deep emerald valleys far below, and vast golden-lit clouds stretching across the horizon.

[Style & Ambiance]: High-budget fantasy cinema aesthetic, photorealistic, shot on 35mm film, matching the visual tone of Part 1. Dramatic golden-hour backlighting as the unicorn leaves the shadowed canopy and enters brilliant, warm sunlight. Volumetric sunbeams, lens flare off the unfurling wings, and swirling mountain mist. Color palette transitions from deep jungle greens to luminous ivory, warm gold, and expansive sky blues.

[Audio]: Rapid hoofbeats transitioning from soft earth to loud clattering on bare rock, followed by sudden silence and the rush of high-altitude wind as it leaves the cliff. SFX: A resonant, crystalline shimmer and a deep, powerful whoosh as the massive wings unfurl and beat against the air. The swelling orchestral strings from Part 1 erupt into a triumphant, soaring cinematic score. No dialogue, no subtitles.

**SCENE 3**
[Cinematography]: Smooth, sweeping aerial tracking shot filmed from a three-quarter front-side angle, gliding effortlessly alongside and slightly below the ascending subject, then slowly orbiting toward a wide side profile. Shot on a 35mm anamorphic lens mounted on a stabilized aerial gimbal, with deep focus keeping both the winged unicorn and the distant mountain peaks crisp, subtle wind-buffeting micro-motion, and natural anamorphic lens flare.

[Subject]: The same majestic, pure-white winged unicorn with a muscular build, a pearlescent, spiraling ivory horn, a long, silky silver-white mane and tail streaming straight back in the slipstream, and massive, radiant white-feathered wings with subtle gold-edged plumage. Faint flecks of dried jungle mud remain on its lower legs. Its four legs are completely still and folded neatly at the knees, tucked tightly and symmetrically close against its underside in the streamlined, aerodynamic posture of a large soaring bird of prey.

[Action]: The winged unicorn climbs steadily higher into the upper sky. Its legs remain motionless and tucked tightly against its body throughout the entire shot, showing zero galloping or paddling movement. All propulsion comes strictly from its massive wings, which execute slow, deep, rhythmic, powerful downstrokes, flexing at the joints and catching the rushing air before gliding smoothly upward through thin wisps of cloud.

[Context]: High altitude above a sprawling, rugged mountain range. Far below, the dense green jungle canopy and jagged granite cliffs recede into miniature scale, partially veiled by a sea of sunlit cumulus clouds. Ahead and above stretches an expansive, open golden-blue sky bathed in high-altitude sunlight.

[Style & Ambiance]: High-budget fantasy cinema aesthetic, photorealistic, shot on 35mm film, maintaining strict visual continuity with Parts 1 and 2. Crisp, radiant golden-hour sunlight illuminating the underside of the beating wings and creating glowing translucent edges through the feathers. Cool atmospheric blue haze in the deep valleys below contrasting with warm amber highlights in the sky.

[Audio]: The steady, rushing sound of high-altitude wind whipping past the camera. SFX: Deep, heavy, rhythmic whooshes of air with each slow, powerful beat of the massive feathered wings, accompanied by the subtle rustle of primary feathers flexing under wind resistance. The triumphant orchestral score swells warmly with French horns and sweeping strings, feeling expansive and majestic. No dialogue, no subtitles.

**SCENE 4**
[Cinematography]: Ultra-smooth, stabilized aerial tracking shot, gliding gracefully parallel to the subject from a slightly elevated side-three-quarter angle, slowly drifting closer into a medium-wide profile. Shot on a 35mm anamorphic lens with deep depth of field, cinematic motion blur on passing cloud wisps to convey high-altitude speed, and razor-sharp focus locked on the gliding unicorn.

[Subject]: The same majestic, pure-white winged unicorn with a muscular build, a pearlescent, spiraling ivory horn, and a long, silky silver-white mane and tail streaming straight backward in the slipstream. Its massive, radiant white-feathered wings with subtle gold-edged plumage are fully extended outward in a wide, graceful span. Both its front and hind legs are completely still, motionless, and tucked neatly and tightly beneath its torso, folded cleanly at the knees in an unbroken, aerodynamic bird-like glide posture.

[Action]: The winged unicorn glides effortlessly through the open sky on thermal air currents without flapping. Its front and hind legs remain completely frozen and motionless against its body for the entire duration of the shot, with zero kicking, paddling, or running motion. Only its outstretched wings make subtle, deliberate micro-adjustments—tilting slightly at the wingtips and flexing individual primary feathers—to steer and stabilize its smooth, level flight through the air.

[Context]: High-altitude open sky far above a vast sea of sunlit, billowing clouds, with distant snow-dusted mountain peaks barely visible on the far horizon. Thin, translucent ribbons of mist and sunlit cloud vapor rush past the unicorn, emphasizing its forward momentum.

[Style & Ambiance]: High-budget fantasy cinema aesthetic, photorealistic, shot on 35mm film, maintaining strict visual continuity with Parts 1, 2, and 3. Serene, radiant golden-hour sunlight bathing the upper surfaces of the wings and creating soft, luminous rim lighting along its pure-white coat, horn, and streaming mane. Clean, tranquil color palette of brilliant ivory, warm gold, soft cloud whites, and deep azure sky.

[Audio]: Tranquil, airy high-altitude atmosphere. Soft, steady rushing wind as the unicorn cuts smoothly through the sky. SFX: The delicate, crisp ruffling and soft fluttering of individual wing feathers catching the breeze during subtle flight adjustments, completely isolated with zero hoofbeats, zero galloping sounds, and zero ground noise. Minimalist, ethereal ambient orchestral pad playing softly underneath to evoke peaceful weightlessness. No dialogue, no subtitles.

**SCENE 5**
[Cinematography]: Sweeping aerial tracking shot that begins in a wide side profile and slowly arcs forward into a dramatic three-quarter front angle as the unicorn flies through dense cloud formations. Shot on a 35mm anamorphic lens with deep depth of field, rich atmospheric haze, and crisp focus locked on the gliding unicorn.

[Subject]: The same majestic, pure-white winged unicorn with a muscular build, a pearlescent, spiraling ivory horn, and a long, silky silver-white mane and tail streaming straight backward in the wind. Its massive, radiant white-feathered wings with subtle gold-edged plumage are stretched wide in a graceful span. Both its front and hind legs remain completely still, motionless, and tucked tightly beneath its torso, folded cleanly at the knees in an aerodynamic bird-like glide posture.

[Action]: The winged unicorn glides smoothly forward into a dense, towering sea of clouds. Its front and hind legs remain completely frozen and motionless against its body throughout the entire clip with zero leg movement. Only its outstretched wings make subtle, deliberate micro-adjustments—tilting gently at the wingtips and flexing individual primary feathers—as it banks slightly and slices cleanly through billowing white cloud banks, trailing swirling wisps of vapor off its wingtips.

[Context]: Surrounded on all sides—above, below, and ahead—by massive, sunlit cumulus cloud formations and drifting layers of misty vapor, creating a dramatic canyon of clouds in the high sky.

[Style & Ambiance]: High-budget fantasy cinema aesthetic, photorealistic, shot on 35mm film, maintaining strict visual continuity with Parts 1 through 4. Warm golden sunlight piercing through gaps in the surrounding clouds, casting shifting beams of light and soft shadows across the unicorn's white coat and feathered wings. Ethereal color palette of luminous ivory, sunlit gold, soft silver-grey cloud shadows, and deep sky blue.

[Audio]: Immersive high-altitude wind rushing steadily past. SFX: The soft, crisp ruffling and delicate fluttering of wing feathers making subtle steering adjustments, paired with a gentle whoosh as the unicorn cuts through dense cloud vapor—completely free of any hoofbeats or galloping sounds. A warm, expansive ambient orchestral score plays softly underneath. No dialogue, no subtitles.

**SCENE 6**
[Cinematography]: Sweeping aerial tracking shot starting in a wide side profile and slowly arcing forward into a three-quarter front angle as the unicorn flies through dense clouds. 35mm anamorphic lens, deep depth of field, rich atmospheric haze, crisp focus on the subject.

[Subject]: The same pure-white winged unicorn with a muscular build, pearlescent spiraling ivory horn, long silky silver-white mane and tail streaming straight backward in the wind, and massive white-feathered wings with subtle gold-edged plumage stretched wide. Both front and hind legs remain completely still, motionless, and tucked tightly against its underside, folded cleanly at the knees like a soaring bird.

[Action]: The winged unicorn glides smoothly forward into a dense, towering sea of clouds. Its front and hind legs stay completely frozen and still against its body for the entire clip with zero leg movement. Only its outstretched wings make subtle micro-adjustments—tilting gently at the wingtips and flexing primary feathers—as it banks slightly and slices through billowing white cloud banks, trailing wisps of vapor off its wingtips.

[Context]: Surrounded on all sides—above, below, and ahead—by massive sunlit cumulus clouds and drifting layers of misty vapor high in the sky.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 4. Warm golden sunlight piercing through cloud gaps, casting shifting light and soft shadows across its white coat and feathered wings. Color palette of luminous ivory, warm gold, soft silver cloud shadows, and deep sky blue.

[Audio]: Steady high-altitude wind rushing past, paired with the delicate, crisp ruffling and soft fluttering of wing feathers making subtle steering adjustments and a gentle whoosh through cloud vapor. Peaceful, airy atmosphere with a soft ambient orchestral score underneath, completely free of any hoofbeats or ground sounds. No dialogue, no subtitles.

**SCENE 7**
[Cinematography]: Sweeping aerial tracking shot starting from a slightly elevated side-three-quarter angle and smoothly drifting behind and above the subject into a wide over-the-wing perspective, revealing the landscape below. 35mm anamorphic lens, deep depth of field, subtle atmospheric haze, and crisp focus locked on the descending unicorn.

[Subject]: The same pure-white winged unicorn with a muscular build, pearlescent spiraling ivory horn, long silky silver-white mane and tail streaming straight backward in the wind, and massive white-feathered wings with subtle gold-edged plumage angled slightly downward for descent. Both front and hind legs remain completely still, motionless, and tucked tightly against its underside, folded cleanly at the knees like a soaring bird.

[Action]: The winged unicorn begins a graceful, controlled glide downward through thinning cloud layers. Its front and hind legs remain completely frozen and still against its body throughout the entire clip with zero leg movement. Its outstretched wings tilt subtly at the shoulders and flex gently at the wingtips to guide its smooth downward angle, banking slightly as the clouds part ahead to reveal a distant lake on the horizon.

[Context]: Breaking through the lower edge of sunlit cumulus clouds into clearer high-altitude air above a vast, lush valley. Far ahead on the distant horizon, the shimmering outline of a large, tranquil lake nestled among rolling green hills and forests gradually comes into view, reflecting the golden sky.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 5. Warm golden-hour sunlight casting soft rim lighting along the unicorn's white coat and feathered wings, while the distant lake glints softly through the blue-gold valley mist. Color palette of luminous ivory, warm amber, soft cloud whites, deep valley greens, and shimmering silver-blue water.

[Audio]: Steady, gentle rush of wind as the unicorn descends through the air, paired with the delicate, crisp ruffling and soft fluttering of wing feathers making subtle steering adjustments. Peaceful, expansive atmosphere with a warm, hopeful orchestral melody swelling softly underneath, completely free of any hoofbeats or ground sounds. No dialogue, no subtitles.


**SCENE 8**
[Cinematography]: Sweeping aerial over-the-wing tracking shot gliding smoothly downward behind and slightly to the side of the descending unicorn, gradually tilting forward to frame both the flying unicorn in the upper-left foreground and the distant lake shoreline below. 35mm anamorphic lens, deep depth of field, soft golden valley haze, and crisp focus locked on the main unicorn while the distant shoreline remains softly veiled in mist.

[Subject]: The same pure-white winged unicorn with a muscular build, pearlescent spiraling ivory horn, long silky silver-white mane and tail streaming straight backward in the wind, and massive white-feathered wings with subtle gold-edged plumage angled gently downward in a steady glide. Both front and hind legs remain completely still, motionless, and tucked tightly against its underside, folded cleanly at the knees like a soaring bird.

[Action]: The winged unicorn glides smoothly lower toward the tranquil lake valley below. Its front and hind legs stay completely frozen and still against its body for the entire clip with zero leg movement, while its outstretched wings make subtle, gentle micro-adjustments at the wingtips to guide its descent. Far below on the grassy shoreline beside the water, the faint, distant silhouettes of a graceful adult female unicorn and a small baby foal unicorn stand side by side, partially obscured by golden morning mist as they look upward toward the sky.

[Context]: A serene, expansive green valley surrounding a calm, mirror-like lake bathed in warm golden-hour sunlight. Soft ribbons of luminous valley fog drift across the grassy shore where the two faint, backlit unicorn silhouettes stand near the water's edge, framed by distant forested hills.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 6. Warm, emotional golden-hour backlighting creating glowing rim light along the descending unicorn's wings and turning the distant mother and baby unicorn into soft, ethereal silhouettes veiled in sunlit mist. Color palette of luminous ivory, warm amber gold, misty silver, lush meadow greens, and calm sapphire water.

[Audio]: Gentle, airy rush of wind as the unicorn descends lower into the valley, paired with the delicate, crisp ruffling and soft fluttering of wing feathers making subtle steering adjustments. Emotional, heartwarming orchestral strings and soft woodwinds swelling gently underneath to evoke reunion and wonder, completely free of any hoofbeats or ground sounds. No dialogue, no subtitles.

**SCENE 9**
[Cinematography]: Smooth aerial tracking shot descending alongside the unicorn just above the meadow grass, gliding down to eye-level and slowing to a gentle, steady medium-wide shot as it touches down. 35mm anamorphic lens, shallow depth of field during the landing, warm golden lens flare, and crisp focus on the reunited unicorns.

[Subject]: The same pure-white winged unicorn with a muscular build, pearlescent spiraling ivory horn, silky silver-white mane and tail, and massive white-feathered wings with subtle gold-edged plumage. Joined by two small, delicate pure-white baby unicorn foals with tiny pearlescent horns, fluffy manes, and slender legs, plus the graceful adult female white unicorn waiting peacefully nearby in the mist.

[Action]:
[00:00-00:03] Descending just feet above the lush grass beside the lake, the winged unicorn smoothly unfolds its tucked legs downward, angles its massive wings backward to catch the air and brake gently, and touches down softly onto the sunlit meadow without stumbling, folding its large feathered wings neatly against its sides.
[00:03-00:08] As the winged unicorn stands tall and lowers its head warmly, two small white baby unicorns emerge from the golden mist, trotting eagerly and playfully across the grass toward it, nuzzling gently against its chest and front legs while the adult female unicorn watches calmly from the shoreline.

[Context]: A tranquil, lush green meadow directly beside a calm, mirror-like lake bathed in warm golden-hour sunlight. Dew-covered grass, wildflowers, and soft ribbons of glowing morning mist drift gently across the shoreline, with forested hills and the shimmering lake reflecting the amber sky in the background.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 7. Warm, radiant golden-hour backlighting illuminating the mist, the soft down of the two baby unicorns, and the newly folded feathered wings. Color palette of luminous ivory, warm amber gold, dewy meadow greens, misty silver, and serene sapphire water.

[Audio]: The soft whoosh of air and a resonant rustle of feathers as the massive wings brake and fold neatly against its body, followed by a gentle thud of hooves landing softly on thick meadow grass. SFX: Light, delicate trotting footsteps in the grass from the two baby unicorns, soft affectionate nickers, and gentle water lapping against the lake shore. The emotional, heartwarming orchestral score reaches a triumphant, peaceful resolution with sweeping strings and warm French horns. No dialogue, no subtitles.


**SCENE 10**
[Cinematography]: Steady, gentle medium-wide shot at eye level with the unicorns, subtly panning slightly right as the unicorn on the right walks forward to join the group in the center. 35mm anamorphic lens, shallow depth of field, warm golden-hour lighting, and crisp focus on all four unicorns and the strawberry patch in the foreground.

[Subject]: Exactly four pure-white unicorns already present in the scene, with no additional unicorns appearing: the large adult winged unicorn standing in the center-left foreground with white-feathered wings folded neatly against its back, the two small white baby unicorn foals standing directly beside it, and the single wingless adult female white unicorn standing on the right side of the grassy hill.

[Action]:
[00:00-00:04] The wingless adult female unicorn on the right walks calmly forward across the sunlit grass to join the winged unicorn and the two baby foals in the center, bringing the family of four closely together beside a lush patch of wild strawberry plants in the foreground.
[00:04-00:08] All four unicorns lower their heads gracefully over the green patch dotted with bright red strawberries and begin feeding peacefully, gently nibbling the leaves and ripe berries while their tails swish lazily in the warm breeze.

[Context]: The sun-dappled grassy hillside overlooking the calm, mist-veiled lake during golden hour. Thick green wild strawberry plants heavy with bright red berries grow right in the foreground meadow grass, with rolling green hills and shimmering water in the background.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching the exact look, lighting, and color grade of the input frame. Warm golden-hour sunlight casting soft rim lighting along their white coats, folded feathered wings, and glossy red strawberries. Color palette of luminous ivory, warm amber gold, meadow greens, ruby red berries, and misty lake water.

[Audio]: Soft footsteps on lush grass as the unicorn from the right joins the group, followed by gentle rustling of leafy strawberry plants and delicate nibbling sounds as all four feed peacefully. Distant lakeside songbirds and a warm, tender orchestral melody playing softly underneath. No dialogue, no subtitles.

**SCENE 11**
[Cinematography]: Slow, graceful crane-up and pull-back shot starting at eye level with the grazing unicorns and rising smoothly into a wide, sweeping aerial view of the lakeside meadow. 35mm anamorphic lens, deep depth of field, warm golden lens flare, and crisp focus on the family of four unicorns.

[Subject]: Exactly four pure-white unicorns already present in the scene, with no additional unicorns appearing: the large adult winged unicorn with pearlescent horn and white-feathered wings folded neatly against its back, the single wingless adult female white unicorn beside it, and their two small white baby unicorn foals with tiny horns and fluffy manes.

[Action]: Standing closely together in a peaceful group, all four unicorns continue grazing calmly on the lush patch of wild strawberry plants. They gently nibble the green leaves and bright red berries, occasionally lifting their heads softly to look at one another or out toward the shimmering lake while their tails swish lazily in the golden evening breeze.

[Context]: The tranquil, sun-dappled grassy hillside beside a calm, mirror-like lake during late golden hour. Thick clusters of leafy green wild strawberry plants dotted with ripe red berries surround their hooves in the foreground, while rolling green hills, drifting ribbons of mist, and the warm amber reflection of the setting sun stretch across the water behind them.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 9. Rich, warm sunset rim lighting glowing along their pure-white coats, folded feathered wings, and glossy red strawberries. Color palette of luminous ivory, deep golden amber, emerald meadow greens, ruby red berries, and serene twilight-blue water.

[Audio]: Gentle rustling of leafy strawberry plants and soft, peaceful nibbling sounds as the four unicorns feed together. SFX: Soft, contented breaths, gentle lapping of lake water along the shore, and distant evening songbirds. A warm, emotional orchestral finale with sweeping strings and soft French horns swells gently to a serene, heartwarming close. No dialogue, no subtitles.


**SCENE 12**
[Cinematography]: Low-angle, water-level suspense tracking shot filmed right at the surface of the lake, slowly creeping forward behind and slightly beside the partially submerged crocodile toward the shoreline. 35mm anamorphic lens with shallow depth of field, keeping the crocodile's eyes and snout razor-sharp in the immediate foreground while the grazing unicorn family on the distant grassy bank remains softly visible across the water.

[Subject]: A massive, giant crocodile with rough, armored pastel-pink and rose-tinted scales, heavily submerged beneath the dark lake water with only its ridged brow, predatory golden-amber eyes, and the top of its long pink snout protruding just above the surface. Farther back on the distant grassy shoreline, the exact four pure-white unicorns—one winged adult unicorn with folded white-feathered wings, one wingless adult female unicorn, and two small baby unicorn foals—stand peacefully together, completely unaware.

[Action]: Floating silently at the surface of the calm lake, the giant pink crocodile remains nearly motionless, gliding forward an inch at a time with stealthy precision as tiny V-shaped ripples spread gently from its snout. Its golden eyes stay locked intensely on the distant shore where the four white unicorns continue grazing calmly on the strawberry patch, oblivious to being watched.

[Context]: The glassy, reflective surface of the tranquil lake during late golden hour, with floating lily pads and subtle evening mist drifting over the water. In the background across the water lies the sun-dappled grassy bank dotted with green strawberry plants and red berries, framed by rolling green hills.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 10. Dramatic golden-hour backlighting casting warm amber reflections across the dark ripples of the lake and highlighting the textured pink scales and wet gleam on the crocodile's snout and brow. Color palette of dusty rose and coral pink, deep reflective teal-blue lake water, warm sunset gold, and luminous ivory on the distant shore.

[Audio]: Eerie, quiet lakeside stillness. Soft, subtle lapping of water against the crocodile's submerged scales and a faint, low underwater rumble as it glides silently through the lake. Distant, muffled rustling of leaves and faint songbirds from the far shore. The warm orchestral music from Part 10 fades into a low, tense, mysterious string drone and subtle bass pulse. No dialogue, no subtitles.


**SCENE 13**
[Cinematography]: Low-angle, water-level tracking shot skimming just inches above the surface of the lake, gliding forward directly behind and slightly beside the partially submerged crocodile as it closes the distance toward the shoreline. 35mm anamorphic lens, shifting rack focus from the crocodile's predatory eyes in the foreground to the grazing unicorn family on the approaching grassy bank.

[Subject]: The massive giant crocodile with rough, armored pastel-pink and rose-tinted scales, silently propelling itself through the dark water with only its ridged brow, golden-amber eyes, and the top of its long pink snout visible above the surface. Ahead on the grassy shoreline, the exact four pure-white unicorns—one winged adult unicorn with folded white-feathered wings, one wingless adult female unicorn, and two small baby unicorn foals—stand peacefully together, completely unaware.

[Action]: The giant pink crocodile swims stealthily and steadily toward the lake shore without making a splash, cutting smoothly through the glassy water and leaving a long, silent V-shaped wake trailing behind its snout. As the shoreline grows noticeably closer, the four pure-white unicorns on the grassy bank remain focused on grazing peacefully on the strawberry patch, unaware of the approaching predator.

[Context]: The dark, mirror-like surface of the lake during late golden hour, transitioning toward the mossy, flower-dotted grassy shoreline where lush green wild strawberry plants heavy with red berries grow near the water's edge, backed by misty rolling hills.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 11. Warm late-golden-hour sunlight reflecting off the dark lake ripples and casting a soft rim light along the crocodile's wet pink scales and the white coats of the unicorns on shore. Color palette of dusty rose and coral pink, deep reflective teal-blue water, warm sunset amber, emerald meadow greens, and luminous ivory.

[Audio]: Tense, quiet lakeside atmosphere. The faint, smooth trickle of water parting silently around the crocodile's snout as it glides closer, with zero splashing. Distant, soft rustling of strawberry leaves and gentle nibbling sounds carrying faintly across the water from the grazing unicorns. Low, suspenseful orchestral strings and a subtle, slow heartbeat-like bass pulse gradually build tension. No dialogue, no subtitles.


**SCENE 14**
[Cinematography]: Medium-wide shot at eye level with the unicorn family in the lakeside meadow, matching the exact framing and positions of the input image, transitioning into a slow, tense push-in toward the lead adult unicorn as it raises its head toward the lake. 35mm anamorphic lens, shallow depth of field, warm late-golden-hour lighting, and crisp focus on the four unicorns.

[Subject]: The exact four pure-white, wingless unicorns already present in the input frame, with zero wings and no additional unicorns appearing: the two adult pure-white unicorns with pearlescent spiraling ivory horns and long silky silver-white manes, alongside their two small white baby unicorn foals with tiny horns and fluffy manes.

[Action]:
[00:00-00:03] Standing together in the strawberry patch beside the lake, all four wingless unicorns are initially grazing peacefully with their heads lowered among the green leaves and red berries.
[00:03-00:08] Suddenly, the larger adult unicorn freezes, snaps its head up sharply with ears pinned forward and nostrils flaring, and stares intensely out toward the calm lake water—sensing hidden danger approaching—while the adult female unicorn immediately raises her head in alarm and nudges the two baby foals protectively behind her.

[Context]: The exact sun-dappled grassy hillside and lush green wild strawberry patch dotted with bright red berries from the input image, overlooking the calm, reflective lake during late golden hour with subtle mist drifting over the water in the background.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching the exact look, lighting, and color grade of the input frame. Warm late-sunset rim lighting casting dramatic shadows across their pure-white coats and the strawberry leaves. Color palette of luminous ivory, deep sunset amber, emerald meadow greens, ruby red berries, and dark reflective twilight-blue lake water.

[Audio]: Soft rustling of strawberry leaves and gentle nibbling abruptly stopping into tense, sudden silence. SFX: A sharp, alert snort and intake of breath from the adult unicorn, subtle rustling of grass as the foals shift nervously behind their mother, and the faint, ominous lapping of ripples against the lake shore. The peaceful music cuts out sharply into a low, suspenseful orchestral string tremolo and tense heartbeat pulse. No dialogue, no subtitles.


**SCENE 15**
[Cinematography]: Wide-angle, dynamic lateral tracking shot moving rapidly alongside the shoreline meadow, framing the lake edge on one side and the open hillside ahead. 35mm anamorphic lens with kinetic handheld urgency, deep depth of field keeping both the charging crocodile and the fleeing unicorn family in sharp focus, and subtle motion blur on kicking grass and dirt.

[Subject]: The massive giant crocodile with rough, armored pastel-pink and rose-tinted scales, fully emerged onto the lakeside grass on thick, muscular legs. Ahead of it across the meadow, the exact four pure-white, wingless unicorns—two adult white unicorns with pearlescent spiraling ivory horns and two small white baby unicorn foals with tiny horns—all completely wingless, with no additional unicorns appearing.

[Action]:
[00:00-00:03] Bursting out of the shallow lake water onto the muddy shoreline, the giant pink crocodile accelerates rapidly across the grass, its heavy body low and muscular legs churning furiously as it charges directly toward the strawberry patch.
[00:03-00:08] Immediately reacting, the four wingless white unicorns wheel around together and break into a fast, urgent gallop up the grassy hillside away from the charging crocodile—with the two adult unicorns flanking and shielding the two smaller baby unicorn foals running swiftly between them.

[Context]: The sun-dappled grassy lakeside meadow and wild strawberry patch during late golden hour. Kicked-up blades of grass, scattered red berries, and splashes of shoreline mud fly into the air as the chase moves from the water's edge toward the rolling green hills.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 13. Dramatic late-golden-hour sunlight casting long, urgent shadows across the meadow and glinting off the crocodile's wet pink scales and the unicorns' streaming silver-white manes and tails. Color palette of dusty rose and coral pink, luminous ivory, emerald meadow greens, warm sunset amber, and dark twilight-blue lake water behind them.

[Audio]: Explosive splashing of water transitioning into heavy, rapid thudding and scraping of the giant crocodile's claws tearing across the grassy ground, overlapping with the urgent, rhythmic galloping of hooves pounding across the meadow. SFX: Short, alarmed snorts from the adult unicorns and rustling grass flying past. Intense, fast-paced orchestral chase music with driving percussion and urgent strings. No dialogue, no subtitles.

**SCENE 16**
[Cinematography]: Wide-angle dynamic tracking shot moving alongside the fleeing unicorns and charging crocodile, transitioning smoothly into a sweeping low-angle upward tilt as the unicorns lift off into the air while keeping the halted crocodile visible in the lower foreground. 35mm anamorphic lens, deep depth of field, warm golden lens flare, and crisp focus on both the ascending unicorn family and the crocodile below.

[Subject]: The exact four pure-white unicorns—two adult white unicorns with pearlescent spiraling ivory horns and two small white baby unicorn foals with tiny horns, with no additional unicorns appearing—all sprouting radiant white-feathered wings with subtle gold-edged plumage from their shoulders (large wings on the two adults, smaller proportional wings on the two foals). Below them on the grass stands the massive giant crocodile with rough, armored pastel-pink and rose-tinted scales.

[Action]:
[00:00-00:03] Galloping rapidly across the sunlit grassy hillside with the giant pink crocodile charging close behind, all four white unicorns simultaneously erupt with shimmering, luminous white-feathered wings unfolding from their shoulders in a soft burst of golden light particles.
[00:03-00:08] With slow, graceful, synchronized wingbeats, all four winged unicorns gently leave the ground and rise steadily upward into the air together—the two adults flanking the two smaller flying foals—while the giant pink crocodile skids abruptly to a halt in the grass below, freezing motionless with its heavy jaw slightly open as it stares upward in stunned silence at the ascending family.

[Context]: The sun-dappled grassy hillside meadow above the tranquil lake during late golden hour. Swirling blades of grass and glowing golden motes drift downward beneath the rising unicorns, with the reflective lake and rolling misty hills stretching across the background.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 14. Dramatic late-golden-hour backlighting shining through the translucent edges of all four pairs of white-feathered wings and casting long sunset shadows across the giant pink crocodile frozen on the meadow below. Color palette of luminous ivory, radiant sunset gold, dusty rose and coral pink, emerald meadow greens, and deep twilight-blue sky.

[Audio]: Urgent galloping hooves and heavy crocodile footsteps abruptly giving way to a resonant, magical shimmer and soft, synchronized whooshes of feathered wings lifting off the grass. SFX: The heavy skidding thud of the giant pink crocodile halting on the turf, followed by quiet, breathless stillness on the ground as wind rushes gently beneath the rising wings. The intense chase music resolves suddenly into a triumphant, soaring, emotional orchestral theme with sweeping strings and warm French horns. No dialogue, no subtitles.


**SCENE 17**
[Cinematography]: Sweeping aerial tracking shot gliding smoothly alongside and slightly behind the ascending unicorn family as they climb higher into the open sky, then slowing into a wide, majestic panoramic shot as they soar gracefully into the distance. 35mm anamorphic lens, deep depth of field, crisp natural clarity, and sharp focus on all four flying unicorns.

[Subject]: The exact four pure-white winged unicorns—two adult white unicorns with pearlescent spiraling ivory horns and large white-feathered wings with subtle gold-edged plumage, alongside their two small white baby unicorn foals with tiny horns and proportional white-feathered wings, with no additional unicorns appearing. All four unicorns have their front and hind legs completely still, motionless, and tucked neatly beneath their torsos in the streamlined, aerodynamic posture of soaring birds.

[Action]: Climbing steadily higher above the valley, the four winged unicorns form a tight, protective V-formation in mid-air—with the two adults flying smoothly on either side of the two smaller foals—and soar gracefully forward into the wide open sky. Their legs remain completely frozen and tucked against their bodies with zero leg movement, propelled by slow, rhythmic, synchronized wingbeats transitioning into an effortless, peaceful glide as they grow smaller against the distant clouds.

[Context]: Expansive, bright high-altitude sky filled with soft, sunlit white cumulus clouds, with the tranquil mirror-like lake, lush green meadow, and rolling forested hills receding far below into miniature scale.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 15. Crisp, natural bright daylight illuminating their pure-white coats, translucent feathered wings, and the white clouds around them, with soft blue atmospheric depth over the valley below. Clean, uplifting color palette of luminous ivory, bright sky blue, crisp cloud white, and lush emerald valley greens.

[Audio]: Steady, airy high-altitude wind rushing softly past, paired with the gentle, rhythmic whooshing and delicate feather rustle of four pairs of wings moving in harmony—completely free of any hoofbeats or ground sounds. A triumphant, heartwarming, sweeping orchestral finale with strings and French horns swells gently to a peaceful, uplifting close as the sound fades softly into the sky. No dialogue, no subtitles.

**SCENE 18**
[Cinematography]: Low-angle, slow-moving medium-wide tracking shot at eye level with the crocodile, following smoothly behind and slightly to the side as it turns away from the hillside and walks back toward the water's edge, ending at water level as it slips beneath the surface. 35mm anamorphic lens, shallow depth of field, warm twilight rim lighting, and crisp focus on the crocodile's textured pink scales.

[Subject]: The massive giant crocodile alone in the frame, featuring rough, armored pastel-pink and rose-tinted scales, thick muscular legs, a long heavy ridged tail, and expressive golden-amber eyes. No unicorns are visible on the ground.

[Action]:
[00:00-00:03] Standing motionless on the grassy hillside where it stopped, the giant pink crocodile slowly lowers its gaze from the empty sky, lets out a deep breath, and turns its massive body heavily around toward the lake shoreline.
[00:03-00:08] Lumbering slowly and steadily down the grassy bank with its heavy tail swaying behind it, the giant pink crocodile wades back into the calm lake water, submerging smoothly until only its ridged brow, golden-amber eyes, and the top of its pink snout glide silently across the glassy surface into the evening mist.

[Context]: The quiet, sun-dappled grassy shoreline and wild strawberry patch beside the tranquil, mirror-like lake during late golden hour transitioning into dusk. Soft ribbons of evening mist drift low over the dark reflective water, framed by misty rolling hills in the background.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 15. Rich, warm late-sunset lighting casting long shadows across the grass and glinting off the crocodile's wet pink scales and gentle water ripples. Color palette of dusty rose and coral pink, deep reflective twilight-blue water, warm sunset amber, and muted evening meadow greens.

[Audio]: Quiet, reflective lakeside atmosphere. Heavy, deliberate footsteps on soft grass and crushed leaves as the giant crocodile turns and walks down the bank, followed by a deep, resonant rumble and a gentle, smooth splash as it enters the water. SFX: Soft water lapping against its armored scales and subtle ripples spreading across the lake. The soaring orchestral music fades into a calm, pensive cello and low woodwind melody, evoking solitude and mystery. No dialogue, no subtitles.

**SCENE 19**
[Cinematography]: Low-angle, water-level medium-wide shot skimming just inches above the glassy lake surface, slowly gliding forward toward the giant crocodile as two small baby crocodiles swim into the frame from the shoreline reeds. 35mm anamorphic lens, shallow depth of field, warm twilight reflections on the water, and crisp focus on the three crocodiles.

[Subject]: The massive giant crocodile with rough, armored pastel-pink and rose-tinted scales, floating calmly with its ridged brow, golden-amber eyes, and long pink snout above the surface. Swimming toward it are two tiny, cute baby crocodiles with matching pastel-pink scales and big golden eyes—one empty-mouthed and eager, and the second baby crocodile proudly holding a small silver fish sideways in its jaws with the tail and head sticking out of its mouth.

[Action]:
[00:00-00:03] Floating quietly in the misty evening lake, the giant pink crocodile pauses as two small pink baby crocodiles emerge from a cluster of lakeside reeds, paddling eagerly across the calm water leaving tiny V-shaped ripples behind them.
[00:03-00:08] The two baby crocodiles swim right up to the giant crocodile's snout, gently bumping and nuzzling against its jaw in affectionate greeting while the second baby crocodile lifts its head slightly, still clutching the small silver fish sticking out of its mouth as if offering its catch.

[Context]: A secluded, peaceful cove of the calm, mirror-like lake at dusk, framed by tall green reeds, floating water lilies, mossy logs, and soft ribbons of evening mist drifting low across the dark reflective water.

[Style & Ambiance]: High-budget fantasy cinema, photorealistic 35mm film matching Parts 1 to 16. Soft dusk and late-sunset twilight casting warm amber and violet reflections across the glassy ripples and highlighting the wet pastel-pink scales of the giant crocodile and its two hatchlings. Color palette of dusty rose and coral pink, shimmering silver fish scales, deep twilight-blue water, emerald reed greens, and warm evening amber.

[Audio]: Tranquil dusk lakeside atmosphere. Soft, gentle paddling and light water ripples as the two baby crocodiles swim across the surface, followed by subtle, affectionate low chirps and soft water lapping as they nuzzle the giant crocodile's snout. Distant evening crickets and frogs begin softly in the reeds, accompanied by a warm, tender, heartwarming orchestral string and woodwind melody. No dialogue, no subtitles.

# steps for scope items 8
**USER PROMPT**
Write prompt to replace the existing on this video. The insrumentation and natural sounds should match the scenery and action

**AGENT RESPONSE**
(For Multi-Clip Generation in Flow)
​0:00 – 0:14 | The Forest Sprint​"Upbeat, adventurous fantasy orchestral music with lively pizzicato strings and light bodhrán percussion. Layered with natural sound effects: fast hoofbeats pounding on dirt and roots, rustling ferns, chirping forest birds, and a sudden dramatic whoosh at the cliff edge."
​"Upbeat, adventurous fantasy orchestral music with lively pizzicato strings and light bodhrán percussion. Layered with natural sound effects: fast hoofbeats pounding on dirt and roots, rustling ferns, chirping forest birds, and a sudden dramatic whoosh at the cliff edge."


​0:14 – 1:12 | Soaring Above the Clouds​"Majestic, uplifting cinematic score featuring sweeping lush string sections, noble French horns, and sparkling harp arpeggios. Blended with crisp high-altitude wind rushing past, rhythmic heavy feathered wingbeats, and an ethereal, airy atmosphere."
​"Majestic, uplifting cinematic score featuring sweeping lush string sections, noble French horns, and sparkling harp arpeggios. Blended with crisp high-altitude wind rushing past, rhythmic heavy feathered wingbeats, and an ethereal, airy atmosphere."


​1:12 – 1:59 | Lakeside Peace & Hidden Danger​"Starts as a peaceful, pastoral fantasy theme with solo wooden flute, soft acoustic guitar, gentle breeze through grass, and calm lakeside ambience. Gradually crossfades into dark, suspenseful cinema underscore with low, pulsing cellos, subtle murky water ripples, and tense silence."
​"Starts as a peaceful, pastoral fantasy theme with solo wooden flute, soft acoustic guitar, gentle breeze through grass, and calm lakeside ambience. Gradually crossfades into dark, suspenseful cinema underscore with low, pulsing cellos, subtle murky water ripples, and tense silence."


​1:59 – 2:29 | The Ambush & Magical Escape​"High-stakes, dramatic action score with thunderous timpani, urgent staccato strings, and a triumphant brass fanfare. Synchronized with loud crashing water splashes, heavy scrambling footsteps on grass, a fierce reptilian snap, and a magical shimmering chime sound as wings unfurl into flight."
​"High-stakes, dramatic action score with thunderous timpani, urgent staccato strings, and a triumphant brass fanfare. Synchronized with loud crashing water splashes, heavy scrambling footsteps on grass, a fierce reptilian snap, and a magical shimmering chime sound as wings unfurl into flight."


​2:29 – 3:00 | Dusk by the Water​"Gentle, emotional, and reflective orchestral outro led by a warm solo cello and delicate felt piano. Accompanied by soft water wading and lapping sounds, peaceful twilight marsh ambience, and faint, tender baby crocodile chirps."
​"Gentle, emotional, and reflective orchestral outro led by a warm solo cello and delicate felt piano. Accompanied by soft water wading and lapping sounds, peaceful twilight marsh ambience, and faint, tender baby crocodile chirps."
