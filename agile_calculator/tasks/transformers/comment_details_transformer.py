from agile_calculator.tasks.transformers.base_transformer import BaseTransformer


class CommentDetailsTransformer(BaseTransformer):
    def run(self, records: list) -> list:
        mapped = []
        for record in records:
            mapped.append(record)
        return mapped
