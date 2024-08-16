# Synthetic Seed Data

## Overview

This folder contains synthetic data generated from large language models, which is then translated into all of the language we are collecting human feedback for (full list is inside the translation notebook file). The primary purpose of this data is for collecting human feedback, although some datasets may also be useful for fine-tuning models.

## File Description

### Aligned Q&A

The ['Aligned Q&A'](https://drive.google.com/file/d/1PsWG5fan3SfZZvTWmEiT-r86F3icuYhL/view?usp=sharing) dataset contains question and answer pairs where the model responds to questions about veganism from a pro-vegan perspective. This dataset is primarily intended to be used for collecting human feedback, but it may also be used for training or fine-tuning models to be more aligned with the interests of animals.

### Controversial Q&A

The ['Controversial Q&A'](https://drive.google.com/file/d/1MtexcMxBIEvjd73zOCeqOcY6wP8eKGly/view?usp=sharing) dataset contains question and answer pairs where the model responds to questions about veganism in a way that is controversial or problematic, which can range anywhere from extremely anti-vegan and anti-animal, all the way through to pro-vegan perspectives that may still be problematic or controversial amongst animal advocates for various reasons. This dataset is purely intended for use in collecting human feedback to train models and is not intended to be used directly for fine-tuning or training large language models.

## Usage

This seed data is intended to be used in conversation collection platforms where users engage in dialogue exchanges. The goal is to gather diverse responses, enhancing the training of AI models through human feedback. Users can select questions in their preferred language and respond either as the AI or as the human participant in the conversation.

### Steps to Use

1. **Load the CSV**: Import the datset into your labelling platform (see the [Human-Feedback-Label-Studio](https://github.com/Open-Paws/Human-Feedback-Label-Studio) repo for our implementation of Label Studio)
2. **Select a Conversation Thread**: Select a conversation thread in your labelling platform.
3. **Respond**: Users take turns responding to the selected question, alternating roles between AI and human.
4. **Collect Feedback**: Gather responses to use as training data for AI models, improving their ability to handle multilingual interactions.

## Contribution

If you wish to contribute additional questions or languages to this seed data, please follow these steps:

1. **Add Questions**: Insert new questions into the `Questions` column and answers into the 'Answers' column.
2. **Specify Languages**: Ensure the corresponding languages are accurately represented in the `Languages` column, in the same format used in the translation notebook found in this folder.
3. **Submit**: Update the respective file and submit a pull request or share the updated file with the project maintainers.

## Language Selection

There are more than [7,000 officially recognised living languages](https://www.ethnologue.com/) and unfortunately due to resource constraints, we don't have the capacity or knowledge required to cover all of them. We therefore selected the languages that we believe we are most likely to find relevant data in and/or find volunteers to help us collect and rank data in.

However, we welcome all languages with open arms and would love to further expand the range of languages we are able to cover. If you speak a language that is not already listed, please [contact us through the submission form on our website](https://www.openpaws.ai/get-involved) with more details so we can work together to ensure your language is added to the project.

## License

This data is provided under an open license, allowing for free use and modification. By contributing, you agree to share your additions under the same terms.

For any questions or further information, please contact the project maintainers.
