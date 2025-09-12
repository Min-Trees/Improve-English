# Improve-English

This repository contains a 90-day English learning plan focused on building
communication skills and gradually introducing IELTS practice. The schedule is
generated programmatically and saved in [`data/90_day_plan.json`](data/90_day_plan.json).

Each day provides:

* 5 new vocabulary items with Vietnamese translations and example sentences.
* A short video for listening and shadowing practice.
* Speaking and writing prompts for daily practice.
* From day 46 onward, an extra IELTS task (listening or reading) is suggested.

To regenerate the plan, run:

```bash
python scripts/generate_plan.py
```

The generated file will contain all data for the 90-day schedule.
