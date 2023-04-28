from typing import List
from . import explainable

def get_recommendations(user_id: int) -> List[str]:
    # TODO:Implement recommendation

    # TODO: Store similarity matrix in db/local file
    
    # TODO: Explainable 
    explaination = explainable.get_explaination(user_id)
    recommended_items = ["item1", "item2", "item3"]
    return {
                user_id: recommended_items,
                explaination: explaination
            }
