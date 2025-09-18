import json

from codebleu import calc_codebleu
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from langchain.evaluation import ExactMatchStringEvaluator


class MetricsCalculator(object):

    def __init__(self):
        self.evaluator = ExactMatchStringEvaluator()

    def calc_code_bleu_score(self, reference, generation, language = "Java"):
        raw_score = self.calc_code_bleu(reference, generation, language)
        score = 0
        if raw_score["ngram_match_score"] > 0:
            score = raw_score["codebleu"]
        return score

    def calc_code_bleu(self, reference, generation, language = "Java"):
        codeBleuResults = calc_codebleu([reference], [generation], lang="java")
        return codeBleuResults

    def calc_bleu(self, reference, generation):
        bleuScore = sentence_bleu(reference, generation, smoothing_function=SmoothingFunction().method4)
        return bleuScore

    def calc_exact_match(self, reference, generation):
        score = self.evaluator.evaluate_strings(
            prediction=generation,
            reference=reference,
        )
        return score["score"]
