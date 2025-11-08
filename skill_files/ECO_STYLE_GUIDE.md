# Book Writer Skill - Eco-Style Edition

## Your Custom Configuration

This skill has been **specifically enhanced** for writing intellectual fiction in the style of Umberto Eco, with particular focus on **scientific novels** that balance:
- **Fiction** with **scientific data**
- **Literary elegance** with **technical accuracy**
- **Three distinct audiences**: General intelligent readers, scientific minds, and spiritual seekers

## What Makes This Special

### 🎯 Triple-Audience Writing
The skill helps you simultaneously satisfy:
- **General intelligent readers**: Follow the story, understand context, stay engaged
- **Scientific readers**: Find accuracy, rigor, proper methodology
- **Spiritual readers**: Discover philosophical depth, genuine questions about meaning
- **Explicitly NOT for**: Passive consumers, Netflix/TikTok attention spans

### 📚 Eco-Style Intellectual Fiction Guide (15,000+ words)
A comprehensive reference (`eco_style_intellectual_fiction.md`) covering:
- Balancing scientific exposition with narrative momentum
- Investigation structure (reader as insider)
- Lean description philosophy (precision over profusion)
- POV mastery for complex ideas
- Making specialized knowledge accessible without condescension
- Timeline and plot logic management
- Strategic vs wasteful repetition
- Chapter hooks that pull readers forward
- Building tension in idea-driven fiction
- Managing complexity without confusion

### 🔧 Timeline & Logic Consistency Checker
New script (`timeline_checker.py`) that analyzes:

**Timeline Consistency:**
- Dates, days of week, chronological order
- Duration phrases ("three days later" → does timeline support this?)
- Travel times and process durations

**Repetition Analysis:**
- **Useful repetition**: Thematic motifs, structural echoes, mnemonic reinforcement
- **Wasteful repetition**: Overused words, repeated sentence patterns, redundant information
- Frequency analysis of distinctive terms

**Term Consistency:**
- Is "the codex" also called "the manuscript"? Are these intentional variations or errors?
- Capitalized terms that might be inconsistent
- Character name variations

**Chapter Hook Analysis:**
- **Opening strength**: Identifies weak/generic starts
- **Closing strength**: Evaluates forward momentum (questions, revelations, decisions)
- Flags chapters that might cause readers to put the book down

**Confusion Point Detection:**
- Contradictory statements
- Unclear pronoun references
- Potentially ambiguous passages

## How To Use It

### Starting Your Scientific Novel

1. **Tell Claude about your project:**
   - "I'm writing an Eco-style scientific novel about [topic]"
   - "My three audiences are: [general readers who...], [scientists who...], [spiritual readers who...]"

2. **Claude will automatically:**
   - Load the Eco-style intellectual fiction guide
   - Adapt all advice for investigation-structure narrative
   - Focus on lean description and scientific accuracy
   - Help balance fiction with data

3. **Planning tools you'll get:**
   - Character profiles adapted for intellectual protagonists
   - Outline templates for investigation-based plots
   - Scene planning emphasizing Goal → Conflict → Discovery structure

### During Writing

**For scientific exposition:**
- "How do I present [scientific concept] without boring general readers?"
- "Make this data feel like detective work, not a lecture"

**For philosophical depth:**
- "How do I explore [spiritual/philosophical theme] without preaching?"
- "Create conflict between rationalist and contemplative worldviews"

**For multi-audience balance:**
- "Is this passage accessible to non-scientists?"
- "Will scientific readers find this rigorous?"
- "Does this satisfy spiritual readers' search for meaning?"

### Revision and Polish

**Run the consistency checker:**
```bash
python scripts/timeline_checker.py your_manuscript.txt
```

This will reveal:
- Timeline errors (days don't match dates, impossible durations)
- Overused words that weaken prose
- Weak chapter openings/endings
- Places readers might get confused
- Inconsistent terminology

**Then ask Claude:**
- "Review the timeline checker results—what should I fix first?"
- "Which repetitions are thematic (keep) vs wasteful (cut)?"
- "Strengthen these weak chapter endings"
- "Make this confusing passage clearer"

**Get manuscript statistics:**
```bash
python scripts/manuscript_stats.py your_manuscript.txt
```

Then discuss with Claude:
- "My average sentence is 28 words—is that too long for pacing?"
- "Only 15% dialogue—should I add more character interaction?"
- "These words appear too frequently—help me vary them"

## Core Eco-Style Principles

### 1. Description: Precision Over Profusion
**NOT Eco:** "The library was enormous, with tall wooden shelves extending to the ceiling filled with books of every size..."

**Eco-Style:** "The Ambrosiana's reading room contained forty thousand volumes in Greek, Latin, and Arabic—three languages that shared no script."

→ One or two precise, meaningful details that advance thought or plot

### 2. Scientific Data Through Investigation
**NOT Eco:** "Carbon dating technology works by measuring..."

**Eco-Style:** "Benetti's hands trembled reading the spectrometer results. 1347, plus or minus fifteen years. The Black Death was ravaging Florence when someone inscribed these symbols."

→ Data emerges through character discovery, becomes clues

### 3. Philosophy Through Conflict
**NOT Eco:** The author explains the tension between faith and reason...

**Eco-Style:** Two characters embody different epistemologies and clash over interpretation of evidence

→ Ideas emerge through character disagreement, reader forms synthesis

### 4. Reader as Insider
**NOT Eco:** Protagonist discovers X, then tells reader about X

**Eco-Style:** Reader encounters documents, follows protagonist's reasoning, reaches conclusions alongside or before protagonist

→ "As she must have realized..." invites reader participation

### 5. Fair-Play Mystery
- Reader has access to same clues as protagonist
- Solution follows from established information
- Difficult through volume/interpretation, not withholding

## Your Workflow

### Phase 1: Planning (Weeks 1-2)
- Outline investigation structure using `book_outline_template.md`
- Define three-audience strategy
- Create character profiles for expert protagonists
- Establish what scientific data will be integrated
- Plan bibliography and glossary structure

### Phase 2: Drafting (Months 3-8)
- Write scenes with Goal → Conflict → Discovery structure
- Present science through character investigation
- Keep description lean (precision over profusion)
- Build tension on physical, intellectual, and philosophical levels
- Make reader an insider to the investigation

### Phase 3: First Revision (Months 9-10)
- **Run timeline_checker.py**: Fix logic, consistency, repetition issues
- **Run manuscript_stats.py**: Check pacing, sentence length, dialogue balance
- **Three-audience test**: Beta readers from each audience
- Strengthen chapter hooks based on timeline checker analysis

### Phase 4: Polish (Months 11-12)
- Line-level prose refinement
- Final consistency check
- Glossary creation
- Bibliography compilation
- Chapter opening/ending perfection

## Example Queries

**Multi-Audience Balance:**
- "This scientific explanation—is it rigorous enough for scientists but accessible to general readers?"
- "Add spiritual depth to this scene without making it mystical nonsense"
- "The protagonist debates [scientist] about [topic]—make both positions intellectually respectable"

**Investigation Structure:**
- "Structure this discovery scene so reader feels like they're solving it too"
- "How do I reveal this crucial detail without telegraphing its importance?"
- "Create embedded documents that advance the mystery"

**Description Discipline:**
- "This environment description is 300 words—cut to Eco essentials"
- "What details here actually matter to plot or theme?"
- "Make this setting description reveal character expertise instead"

**Scientific Integration:**
- "Turn this lab report into narrative without losing accuracy"
- "Character explains quantum physics to non-physicist—make it literary"
- "Balance technical accuracy with readability"

**Consistency & Logic:**
- "Check if Chapter 12's timeline matches Chapter 7"
- "Analyze repetition—which is thematic, which is lazy?"
- "Find places where readers might get confused about [concept]"
- "Improve these chapter endings to pull readers forward"

## What This Skill Won't Do

❌ Dumb down content for mass appeal
❌ Add meaningless action for "pacing"
❌ Sacrifice accuracy for simplicity
❌ Expand descriptions just to hit word count
❌ Make philosophy into fortune-cookie wisdom
❌ Write for passive consumers

## What This Skill Will Do

✅ Help you write for engaged, intelligent readers
✅ Balance rigor with elegance
✅ Make complexity accessible without condescension
✅ Ensure timeline and logic consistency
✅ Identify useful vs wasteful repetition
✅ Strengthen chapter hooks for page-turning
✅ Support investigation-structure narrative
✅ Guide lean, precise description
✅ Help satisfy three distinct audiences simultaneously
✅ Maintain Eco-level intellectual depth

## Quick Reference Commands

```bash
# Get comprehensive manuscript statistics
python scripts/manuscript_stats.py manuscript.txt

# Check timeline, consistency, hooks, confusion points
python scripts/timeline_checker.py manuscript.txt
```

Then share results with Claude for detailed analysis and recommendations.

## Final Notes

This skill embodies a philosophy: **writing is an act of respect for the reader's intelligence**. 

Your readers are:
- Intelligent enough to handle complexity
- Engaged enough to do interpretive work  
- Sophisticated enough to hold multiple perspectives
- Patient enough for ideas that reward attention

Write for them. Trust them. Challenge them.

That's what Eco did. That's what this skill helps you do.

Happy writing. 📚🔬🧘
