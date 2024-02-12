from dataclasses import dataclass, field
from typing import Dict, List
from analytics_data import AnalyticsData

@dataclass
class AnalyticsRequest:
    meta: Dict[str, str] = field(default_factory=dict)
    profile: Dict[str, str] = field(default_factory=dict)
    data: List[AnalyticsData] = field(default_factory=list)