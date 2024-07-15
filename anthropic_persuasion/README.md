# Anthropic Persuasion Dataset

The [Anthropic Persuasion Dataset](https://huggingface.co/datasets/Anthropic/persuasion) contains claims and corresponding human-written and model-generated arguments, along with persuasiveness scores. This dataset was created for research on measuring the persuasiveness of language models, as described in this blog post: [Measuring the Persuasiveness of Language Models](https://www.anthropic.com/news/measuring-model-persuasiveness).

## Dataset Summary

The dataset consists of claims and arguments designed to study and measure the persuasiveness of language models. It includes both human and model-generated arguments, with initial and final ratings provided by participants after evaluating the arguments. We have filtered this dataset for the two questions most relevant to veganism and/or animal rights, namely whether or not cultured meat should be allowed to be sold (highly relevant) and whether or not corporates should have to disclose their environmental impact (moderately related).

## Dataset Description

The dataset is provided in a CSV file with the following columns:

- `ID`: The unique identifier for each entry.
- `claim`: The claim for which the argument was generated.
- `argument`: The generated argument, either by a human or a language model.
- `source`: The source of the argument (model name or "Human").
- `prompt_type`: The prompt type used to generate the argument.
- `rating_initial`: The participant's initial rating of the claim.
- `rating_final`: The participant's final rating of the claim after reading the argument.
- `persuasiveness_metric`: A metric to evaluate the persuasiveness of the argument.

## License

This dataset is provided under the Creative Commons Attribution Non Commercial Share Alike 4.0 license (cc-by-nc-sa-4.0). You are free to:

- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material.

Under the following terms:

- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **Non-Commercial**: You may not use the material for commercial purposes.
- **ShareAlike**: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For more details, visit the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

