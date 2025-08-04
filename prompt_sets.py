# USED FOR ORGANIZING PROMPTS

# 5 different LLMs were asked for 8 prompts using the same queries:

# Generic
# You are designing abstract descriptors to help a vision-language model (CLIP) distinguish between real and fake human face images. Generate 8 short prompts (1–3 words each) that express authenticity or naturalness in real face images. Then, generate 8 short prompts (1–3 words each) that express strangeness, vagueness, or anomalies in fake face images. Avoid technical terms.

# Technical
# You are a computer vision expert creating prompts to help a vision-language model (CLIP) detect visual artifacts in synthetic faces. First, generate 8 short prompts (max 6 words each) that describe clean, well-formed, realistic visual traits typical of real face images (e.g., "natural gradients", "consistent lighting"). Then, generate 8 short prompts that describe technical flaws or artifacts often found in deepfakes (e.g., "compression artifacts", "aliasing at edges"). Use common terms from digital imaging, and keep the prompts concise—no full sentences.

# Forensic
# You are a forensic image analyst generating brief descriptors for identifying real versus fake human faces in forensic contexts. First, list 8 short forensic-style prompts (no more than 8 words) that describe normal, anatomically consistent features seen in real faces (e.g., "symmetrical eye alignment", "plausible facial shadows"). Then, list 8 forensic prompts that describe inconsistencies or anatomical anomalies common in fake images (e.g., "asymmetrical ears", "blended texture regions"). Keep the language formal but short. Avoid full sentences.

# Layman
# You are an average social media user describing face images that feel either genuine or suspicious. First, generate 8 short prompt phrases (max 8 words) that reflect a gut feeling that a face is real (e.g., "this looks like a real person", "seems natural to me"). Then, generate 8 casual prompt phrases that reflect intuition that something is off or fake (e.g., "this looks kinda weird", "something feels off"). Use plain, casual English—no technical or forensic language.

# keep the output in this format:
# "prompts": {
#   "real": [...],
#   "fake": [...]
# }

def get_chatgpt4o_prompts():
    return {
        "generic": {
			"real": [
				"warm smile",
				"clear eyes",
				"natural glow",
				"soft expression",
				"balanced features",
				"genuine emotion",
				"smooth texture",
				"relaxed gaze"
			],
			"fake": [
				"hollow gaze",
				"plastic skin",
				"weird smile",
				"blended lines",
				"off symmetry",
				"ghostly look",
				"strange warmth",
				"dreamlike face"
			]
		},
        "technical":  {
			"real": [
				"natural skin texture",
				"consistent lighting",
				"sharp facial features",
				"realistic eye reflections",
				"smooth color gradients",
				"well-defined contours",
				"balanced skin tones",
				"natural depth of field"
			],
			"fake": [
				"compression artifacts",
				"aliasing at edges",
				"blurry transitions",
				"inconsistent lighting",
				"unnatural skin blur",
				"asymmetrical facial features",
				"distorted background edges",
				"mismatched reflections"
			]
		},
        "forensic": {
			"real": [
				"symmetrical eye alignment",
				"consistent skin pore distribution",
				"natural hairline transition",
				"plausible facial shadows",
				"realistic scleral reflections",
				"aligned nasolabial folds",
				"normal ear positioning",
				"uniform lighting across face"
			],
			"fake": [
				"asymmetrical ears",
				"blended texture regions",
				"mismatched eye reflections",
				"inconsistent skin smoothing",
				"irregular hair artifacts",
				"off-angle facial symmetry",
				"deformed or missing teeth",
				"distorted eyeglass frames"
			]
		},
        "layman": {
			"real": [
				"this looks like a real person",
				"feels like someone I could know",
				"seems natural to me",
				"looks totally normal",
				"pretty sure this is a real face",
				"nothing weird about this one",
				"looks like a legit selfie",
				"I’d swipe right on this"
			],
			"fake": [
				"this looks kinda weird",
				"something feels off",
				"face seems a bit messed up",
				"eyes are doing something strange",
				"looks a little too perfect",
				"mouth feels wrong somehow",
				"uncanny vibe going on here",
				"feels like a bad photoshop"
			]
		}
    }

def get_chatgpt4pt5_prompts():
    return {
        "generic": {
			"real": [
				"warm gaze",
				"natural smile",
				"soft wrinkles",
				"clear eyes",
				"relaxed expression",
				"balanced symmetry",
				"authentic texture",
				"lifelike glow"
			],
			"fake": [
				"empty stare",
				"frozen smile",
				"blurred edges",
				"uneven symmetry",
				"plastic skin",
				"strange shadows",
				"vague details",
				"ghostly features"
			]
		},
        "technical": {
			"real": [
				"consistent lighting",
				"natural skin texture",
				"smooth color gradients",
				"precise edge details",
				"realistic reflections",
				"clear depth of field",
				"balanced shadows",
				"accurate facial symmetry"
			],
			"fake": [
				"compression artifacts",
				"color banding",
				"aliasing at edges",
				"blurred texture transitions",
				"specular highlight inconsistencies",
				"unnatural symmetry",
				"flattened depth of field",
				"pixelated details"
			]
		},
        "forensic": {
			"real": [
				"symmetrical facial proportions",
				"consistent skin texture",
				"natural shadow placement",
				"uniform eye reflections",
				"anatomically correct ears",
				"realistic hair transitions",
				"precise lip alignment",
				"accurate nasal symmetry"
			],
			"fake": [
				"misaligned pupil directions",
				"unnatural skin blending",
				"irregular ear shapes",
				"inconsistent shadow angles",
				"distorted hair outlines",
				"blurred lip contours",
				"nose bridge irregularities",
				"eyes lacking realistic highlights"
			]
		},
        "layman": { 
			"real": [
				"looks like a real person",
				"this face seems genuine",
				"feels natural to me",
				"nothing suspicious here",
				"looks totally normal",
				"I think this one's real",
				"seems like an actual photo",
				"this feels authentic"
			],
			"fake": [
				"something feels off",
				"looks kinda weird",
				"this doesn't seem right",
				"feels fake to me",
				"gives me an odd vibe",
				"this face looks unnatural",
				"seems artificial somehow",
				"makes me uncomfortable"
			]
		}
    }

def get_deepseekr1_prompts():
    return {
        "generic":	{
			"real": [
				"natural expression",
				"human warmth",
				"lifelike skin",
				"genuine emotion",
				"organic imperfections",
				"authentic gaze",
				"subtle textures",
				"unposed moment"
			],
			"fake": [
				"plastic sheen",
				"uncanny smoothness",
				"lifeless eyes",
				"blurred anomalies",
				"distorted proportions",
				"glassy skin",
				"weird artifacts",
				"synthetic aura"
			]
		},
        "technical": {
			"real": [
				"natural skin texture",
				"consistent lighting direction",
				"smooth tonal transitions",
				"accurate facial symmetry",
				"precise eye reflections",
				"detailed hair strands",
				"soft shadow gradients",
				"realistic pore variation"
			],
			"fake": [
				"inconsistent skin texture",
				"asymmetrical facial features",
				"blurred edge artifacts",
				"unnatural eye reflections",
				"compression banding artifacts",
				"mismatched lighting angles",
				"distorted hair details",
				"color inconsistency patches"
			]
		},
        "forensic": {
			"real": [
				"Bilateral facial symmetry",
				"Consistent skin texture",
				"Anatomically correct eye reflections",
				"Natural hair follicle patterns",
				"Plausible shadow transitions",
				"Proportional feature spacing",
				"Cohesive wrinkle continuity",
				"Harmonious lighting gradients"
			],
			"fake": [
				"Asymmetrical ear positioning",
				"Inconsistent skin porosity",
				"Mismatched eye reflections",
				"Aberrant hair strand generation",
				"Illogical shadow directions",
				"Disproportionate facial landmarks",
				"Discontinuous wrinkle patterns",
				"Incoherent lighting sources"
			]
		},
        "layman": {
			"real": [
				"This looks like a real person",
				"Seems totally natural to me",
				"Just a normal everyday face",
				"Could be someone's profile picture",
				"Feels like a genuine photo",
				"Nothing weird about this one",
				"Looks like a regular human",
				"I'd see this person walking around"
			],
			"fake": [
				"Something feels off about this",
				"This looks kinda weird and artificial",
				"Face seems too smooth or perfect",
				"Gives me uncanny valley vibes",
				"Looks like a video game character",
				"Feels like a bad photoshop job",
				"That doesn't look quite right",
				"My gut says this is fake"
			]
		}
    }

def get_gemini2pt5pro_prompts():
    return {
        "generic": {
			"real": [
				"Natural light",
				"Real skin texture",
				"Slight asymmetry",
				"Genuine emotion",
				"Expressive eyes",
				"Fine hair strands",
				"Normal blemishes",
				"Warm skin tone"
			],
			"fake": [
				"Uncanny look",
				"Plastic skin",
				"Too perfect",
				"Strange artifacts",
				"Vacant stare",
				"Melted hair",
				"Odd background",
				"Flat lighting"
			]
		},
        "technical": {
			"real": [
				"Natural skin texture and pores",
				"Fine vellus hair details",
				"Consistent global illumination",
				"Coherent shadows and highlights",
				"Natural color space gradients",
				"Sharp, detailed eye reflections",
				"Organic depth of field",
				"Subtle, natural facial asymmetry"
			],
			"fake": [
				"Unnatural waxy skin smoothing",
				"Geometric warping or distortion",
				"Inconsistent directional lighting",
				"Aliasing artifacts on edges",
				"Noticeable image compression noise",
				"Strange incoherent background patterns",
				"Mismatched or blank eye reflections",
				"Digital color banding artifacts"
			]
		},
        "forensic": {
			"real": [
				"Consistent iris patterns and reflections.",
				"Natural skin texture with fine pores.",
				"Logically cast shadows from facial features.",
				"Symmetrical placement of ears and eyes.",
				"Age-appropriate skin elasticity and wrinkles.",
				"Realistic hair follicle and strand detail.",
				"Coherent lighting across entire facial region.",
				"Naturally aligned teeth and gum lines."
			],
			"fake": [
				"Unnatural smoothness or blurred skin textures.",
				"Asymmetrical ear shapes and positioning.",
				"Inconsistent lighting on facial planes.",
				"Distorted background elements near the head.",
				"Mismatched iris patterns or pupil details.",
				"Illogical hair strands or hairline blending.",
				"Anomalous or warped spectacle frames.",
				"Perfectly uniform, unnatural teeth structure."
			]
		},
        "layman": {
			"real": [
				"this looks like a real person",
				"seems natural and authentic to me",
				"just a normal, everyday photo",
				"nothing seems out of place here",
				"yep, this is a genuine picture",
				"looks like a totally normal selfie",
				"this person definitely seems real",
				"I believe this is a real photo"
			],
			"fake": [
				"this looks kinda weird to me",
				"something about this face feels off",
				"hmm, this doesn't look quite right",
				"getting a weird vibe from this photo",
				"this feels a little fake or edited",
				"the eyes look a little strange",
				"is this even a real person?",
				"this has that weird AI look"
			]
		}
    }

def get_claudesonnet4_prompts():
    return {
        "generic": {
			"real": [
				"natural skin",
				"lived expression",
				"genuine smile",
				"weathered features",
				"asymmetric face",
				"warm eyes",
				"subtle imperfections",
				"human warmth"
			],
			"fake": [
				"uncanny valley",
				"plastic appearance",
				"hollow stare",
				"artificial smoothness",
				"strange proportions",
				"lifeless expression",
				"eerie perfection",
				"robotic features"
			]
		},
        "technical": {
			"real": [
				"natural skin texture variations",
				"consistent lighting across features",
				"smooth color gradients",
				"proper shadow depth mapping",
				"organic facial asymmetry",
				"realistic pore detail distribution",
				"coherent reflection patterns",
				"natural motion blur edges"
			],
			"fake": [
				"compression artifacts around eyes",
				"aliasing at hair boundaries",
				"temporal flickering between frames",
				"inconsistent illumination mapping",
				"blocky pixel transitions",
				"unnatural color bleeding",
				"geometric distortion patterns",
				"pixelated edge discontinuities"
			]
		},
        "forensic": {
			"real": [
				"consistent facial proportions and symmetry",
				"natural skin texture with pore visibility",
				"coherent lighting across all facial features",
				"anatomically correct eye spacing and alignment",
				"realistic shadow casting from nose bridge",
				"uniform hair strand direction and thickness",
				"proper depth perception in facial contours",
				"natural color gradation in skin tones"
			],
			"fake": [
				"misaligned pupils or iris irregularities",
				"inconsistent lighting between facial regions",
				"blurred boundaries around hairline edges",
				"asymmetrical ear positioning or morphology",
				"artificial smoothness lacking skin texture",
				"color bleeding between adjacent facial areas",
				"distorted facial feature proportional relationships",
				"unnatural shadow patterns contradicting light source"
			]
		},
        "layman": {
			"real": [
				"this looks like a real person",
				"seems natural to me",
				"looks totally normal",
				"just a regular photo",
				"nothing weird about this face",
				"looks like someone I'd know",
				"seems genuine and authentic",
				"typical everyday person photo"
			],
			"fake": [
				"this looks kinda weird",
				"something feels off here",
				"face looks too perfect somehow",
				"eyes seem strange to me",
				"doesn't look quite right",
				"something about this seems fake",
				"looks artificial or computer made",
				"gives me uncanny valley vibes"
			]
		}
    }