# Enhancing Graph-to-Text Systems in Low-Resource Settings: Distilling Chain-of-Thought Reasoning for Task-Specific Worflows

Here we present the code that can be used to replicate our experiments for our final report, Enhancing Graph-to-Text Systems in Low-Resource Settings: Distilling Chain-of-Thought Reasoning for Task-Specific Worflows. All the preprocessing and fine-tuning steps can be found in the notebooks given in the following folders:

1. [PLMs finetuned for data to text](https://github.com/davidguzmanp/Graph-to-Text-LLM-with-dataset-augmentation/tree/main/1.%20PLMs%20finetuned%20for%20data%20to%20text): We pre-train and fine-tune a FLAN-T5-small model on the 2017 version of WebNLG dataset for the graph-to-text task. We evaluate the performance using the BLEU, NLTK BLEU and chrF++ metrics. This is a reproduction of the paper: "[Investigating Pretrained Language Models for Graph-to-Text Generation](https://arxiv.org/pdf/2007.08426.pdf)", EMNLP | NLP4ConvAI.
2021a).

2. [Adapter, PLM with GNN for data to text](https://github.com/davidguzmanp/Graph-to-Text-LLM-with-dataset-augmentation/tree/main/2.%20Adapter%2C%20PLM%20with%20GNN%20for%20data%20to%20text): Our attempt to reproduce the GNN adapter model from the paper: ["Structural Adapters in Pretrained Language Models for AMR-to-Text Generation"](https://arxiv.org/pdf/2103.09120.pdf)

3. [Knowledge tansfer, PLM finetuned on different data to text tasks](https://github.com/davidguzmanp/Graph-to-Text-LLM-with-dataset-augmentation/tree/main/3.%20Knowledge%20tansfer%2C%20PLM%20finetuned%20on%20different%20data%20to%20text%20tasks%20): In an effort to harness the potential of multi-task learning, we incorporated supplementary tasks that bear a similar fundamental structure to our primary graph-to-text task. We train FLAN-T5-base models on (1) [WebNLG 2020](https://synalp.gitlabpages.inria.fr/webnlg-challenge/challenge_2020/), (2) [DART](https://github.com/Yale-LILY/dart), (3) A mixed dataset of [WebNLG 2020](https://synalp.gitlabpages.inria.fr/webnlg-challenge/challenge_2020/), [DART](https://github.com/Yale-LILY/dart) and [E2E](https://github.com/tuetschek/e2e-dataset). Then we evaluate the performances of the three datasets separately.

4. [Dataset augmentation via prompt engineering](https://github.com/davidguzmanp/Graph-to-Text-LLM-with-dataset-augmentation/tree/main/4.%20Dataset%20augmentation%20via%20prompt%20engineering):  Inspired from the paper ["Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"](https://arxiv.org/abs/2201.11903) and knowledge distillation techniques (["Textbooks Are All You Need"](https://arxiv.org/abs/2306.11644)), we built a pipelined model to infuse chain-of-thought reasoning into T5 small and base models on the [WebNLG 2020](https://synalp.gitlabpages.inria.fr/webnlg-challenge/challenge_2020/) dataset for graph-to-text generation.

## Datasets

In our experiments, we use the following datasets: [WebNLG 2017](https://webnlg-challenge.loria.fr/challenge_2017/), [WebNLG 2020](https://synalp.gitlabpages.inria.fr/webnlg-challenge/challenge_2020/), [DART](https://github.com/Yale-LILY/dart), [E2E](https://github.com/tuetschek/e2e-dataset)

## Metrics

For our experiments, we use the following metrics: [BLEU, NLTK BLEU, chrF++](https://github.com/WebNLG/GenerationEval) and [BERT score](https://github.com/Tiiiger/bert_score).

* You can also find our notebooks with the cell outputs, training multiple models on multiple outputs [in our legacy code folder](https://github.com/davidguzmanp/Graph-to-Text-LLM-with-dataset-augmentation/tree/main/legacy)
