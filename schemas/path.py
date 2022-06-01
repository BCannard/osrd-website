from typing import List, Optional

from geojson_pydantic import Point
from pydantic import BaseModel

from osrd_infra.schemas.infra import (
    DirectionalTrackRange,
    ObjectReference,
    TrackLocationTrait,
)


class GeometryPointTrait(BaseModel):
    geo: Point = Field(description="this is the type of trait and is charactherized by geometric coordinates")
    sch: Point = Field(description="this is the type of trait and is charactherized by schematic coordinates")


class RoutePath(BaseModel):
    route: ObjectReference
    track_sections: List[DirectionalTrackRange]


class PathWaypoint(GeometryPointTrait, TrackLocationTrait):
    name: Optional[str]
    suggestion: bool
    duration: float


class PathPayload(BaseModel):
    route_paths: List[RoutePath]
    path_waypoints: List[PathWaypoint]


class SlopePoint(BaseModel):
    position: float
    gradient: float


class Slopes(BaseModel):
    __root__: List[SlopePoint]


class CurvePoint(BaseModel):
    position: float
    radius: float


class Curves(BaseModel):
    __root__: List[CurvePoint]
