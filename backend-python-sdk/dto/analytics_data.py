from dataclasses import dataclass, field
from typing import List, Optional

from ..entities.analytics_property import AnalyticsProperty

@dataclass
class AnalyticsData:
    event_action: Optional[str] = None
    timestamp: Optional[str] = None
    event_type: Optional[str] = None
    properties: List[AnalyticsProperty] = field(default_factory=list)