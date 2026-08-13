import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from recommender.scoring import FileScorer
from models.recommendation_model import Recommendation


class RecommendationEngine:

    def __init__(self):

        self.scorer = FileScorer()

    def generate(
        self,
        files
    ):

        recommendations = []

        for file in files:

            score = self.scorer.calculate_score(
                file
            )

            action = self._determine_action(
                score
            )

            reason = self._generate_reason(
                file,
                score
            )

            recommendations.append(

                Recommendation(
                    file=file,
                    action=action,
                    confidence=score,
                    reason=reason
                )
            )

        return sorted(
            recommendations,
            key=lambda x: x.confidence,
            reverse=True
        )

    def _determine_action(
        self,
        score
    ):

        if score >= 70:
            return "CLEAN"

        if score >= 40:
            return "ARCHIVE"

        if score >= 20:
            return "REVIEW"

        return "KEEP"

    def _generate_reason(
        self,
        file,
        score
    ):

        reasons = []

        if file.is_duplicate:
            reasons.append(
                "duplicate file"
            )

        size_mb = (
            file.size /
            (1024 * 1024)
        )

        if size_mb > 100:
            reasons.append(
                "large file"
            )

        if not reasons:
            reasons.append(
                "normal usage pattern"
            )

        return ", ".join(reasons)