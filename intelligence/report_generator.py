import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from intelligence.importance_scorer import (
    ImportanceScorer
)

from intelligence.risk_assessor import (
    RiskAssessor
)


class ReportGenerator:

    def __init__(self):

        self.importance = (
            ImportanceScorer()
        )

        self.risk = (
            RiskAssessor()
        )

    def generate_report(
        self,
        recommendations
    ):

        report = []

        for rec in recommendations[:20]:

            importance = (
                self.importance.calculate(
                    rec.file
                )
            )

            risk = (
                self.risk.assess(
                    rec.file,
                    importance
                )
            )

            report.append({

                "file":
                    rec.file.name,

                "action":
                    rec.action,

                "importance":
                    importance,

                "risk":
                    risk,

                "reason":
                    rec.reason,
            })

        return report