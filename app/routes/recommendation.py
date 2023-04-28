# Contains the API endpoints
from fastapi import APIRouter
from app.models import content_based, collaborative_filtering
from pydantic import BaseModel

router = APIRouter()

class RecommendParams(BaseModel):
    user_id: int
    algo: str

@router.post("/recommend")
async def recommend(params: RecommendParams):
    if params.algo == 'content_based':
        recommended_items = content_based.get_recommendations(params.user_id)
    elif params.algo == 'collaborative_filtering':
        recommended_items = collaborative_filtering.get_recommendations(params.user_id)
    else:
        recommended_items = []
    return {"recommended_items": recommended_items}

# class EvaluationParams:
#     algo: str

@router.get("/evaluation")
async def evaluation(algo:str):
    if algo=='content_based':
        #TODO: Evaluate
        matric = {
            "precession": '80%',
            "recall": '90%'
        }
        return {
            "model": algo,
            "matric": matric
        }


