from agile_calculator.records.transformed.lead_time_for_changes_record import (
    LeadTimeForChangesRecord,
)


class LeadTimeForChangesTransformer:
    def run(self, records):
        # TODO: 
        # merged_dateごとにlead_time_secondsの平均を算出
        # merged_dict = defaultdict(list)
        # for r in records:
        #     merged_dict[r.merged_date].append(r.lead_time_seconds)
        # # 日付でソートし、平均値を算出
        # sorted_items = sorted((k, mean(v)) for k, v in merged_dict.items())
        for record in records:
            if not record.merged_at:
                continue
            lead_time_seconds = (record.merged_at - record.created_at).total_seconds()
            yield LeadTimeForChangesRecord(
                number=record.number,
                title=record.title,
                merged_date=record.merged_at.date(),
                lead_time_seconds=lead_time_seconds
        )
