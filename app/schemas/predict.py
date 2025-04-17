from typing import Any, List, Optional, Union
import datetime

from pydantic import BaseModel, Field


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[float]

class DataInputSchema(BaseModel):
    Id: int
    MSSubClass: int
    MSZoning: str
    LotFrontage: Optional[float]
    LotArea: int
    Street: str
    Alley: Optional[str] = None
    LotShape: str
    LandContour: str
    Utilities: str
    LotConfig: str
    LandSlope: str
    Neighborhood: str
    Condition1: str
    Condition2: str
    BldgType: str
    HouseStyle: str
    OverallQual: int
    OverallCond: int
    YearBuilt: int
    YearRemodAdd: int
    RoofStyle: str
    RoofMatl: str
    Exterior1st: str
    Exterior2nd: str
    MasVnrType: Optional[str]
    MasVnrArea: Optional[float]
    ExterQual: str
    ExterCond: str
    Foundation: str
    BsmtQual: Optional[str]
    BsmtCond: Optional[str]
    BsmtExposure: Optional[str]
    BsmtFinType1: Optional[str]
    BsmtFinSF1: int
    BsmtFinType2: Optional[str]
    BsmtFinSF2: int
    BsmtUnfSF: int
    TotalBsmtSF: int
    Heating: str
    HeatingQC: str
    CentralAir: str
    Electrical: Optional[str]
    FirstFlrSF: int = Field(..., alias='1stFlrSF')
    SecondFlrSF: int = Field(..., alias='2ndFlrSF')
    LowQualFinSF: int
    GrLivArea: int
    BsmtFullBath: int
    BsmtHalfBath: int
    FullBath: int
    HalfBath: int
    BedroomAbvGr: int
    KitchenAbvGr: int
    KitchenQual: str
    TotRmsAbvGrd: int
    Functional: str
    Fireplaces: int
    FireplaceQu: Optional[str]
    GarageType: Optional[str]
    GarageYrBlt: Optional[int]
    GarageFinish: Optional[str]
    GarageCars: int
    GarageArea: int
    GarageQual: Optional[str]
    GarageCond: Optional[str]
    PavedDrive: str
    WoodDeckSF: int
    OpenPorchSF: int
    EnclosedPorch: int
    ThreeSsnPorch: int = Field(..., alias='3SsnPorch')
    ScreenPorch: int
    PoolArea: int
    PoolQC: Optional[str] = None
    Fence: Optional[str] = None
    MiscFeature: Optional[str] = None
    MiscVal: int
    MoSold: int
    YrSold: int
    SaleType: str
    SaleCondition: str

    class Config:
        populate_by_name = True

class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]