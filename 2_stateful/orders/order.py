from dataclasses import dataclass
from dataclasses import field

@dataclass
class LineItem:
    description: str
    price: int
    quantity: int
    
    @property
    def total(self) -> int:
        return self.price * self.quantity

@dataclass
class Order:
    customer: str
    line_items: list[LineItem] = field(default_factory=list)
    _total_cache: int = 0
    
    def __post_init__(self) -> None:
        self._update_total_cache()
    
    def _update_total_cache(self):
        self._total_cache = sum(li.total for li in self.line_items)
    
    def add_line_item(self, line_item: LineItem) -> None:
        # self.line_items.append(line_item)
        # self._total_cache += line_item.total
        if line_item not in self.line_items:
            self.line_items.append(line_item)
        self._update_total_cache()
    
    def remove_line_item(self, line_item: LineItem) -> None:
        # self._total_cache -= line_item.total
        self.line_items.remove(line_item)
        self._update_total_cache()
    
    def update_li_quantity(self, line_item: LineItem, quantity: int) -> None:
        line_item.quantity = quantity
        self._update_total_cache()
        
    
    @property
    def total(self) -> int:
        return self._total_cache
        