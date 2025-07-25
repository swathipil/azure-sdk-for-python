# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    AgeMismatchInference,
    Annotation,
    AssessmentValueRange,
    CodeableConcept,
    Coding,
    CompleteOrderDiscrepancyInference,
    CriticalResult,
    CriticalResultInference,
    DocumentAdministrativeMetadata,
    DocumentAuthor,
    DocumentContent,
    DomainResource,
    Element,
    Extension,
    FindingInference,
    FindingOptions,
    FollowupCommunicationInference,
    FollowupRecommendationInference,
    FollowupRecommendationOptions,
    GenericProcedureRecommendation,
    GuidanceInference,
    GuidanceOptions,
    HealthInsightsErrorResponse,
    Identifier,
    ImagingProcedure,
    ImagingProcedureRecommendation,
    LateralityDiscrepancyInference,
    LimitedOrderDiscrepancyInference,
    Meta,
    Narrative,
    Observation,
    ObservationComponent,
    ObservationReferenceRange,
    OrderedProcedure,
    PatientDetails,
    PatientDocument,
    PatientEncounter,
    PatientRecord,
    Period,
    PresentGuidanceInformation,
    ProcedureRecommendation,
    QualityMeasureInference,
    QualityMeasureOptions,
    Quantity,
    RadiologyCodeWithTypes,
    RadiologyInsightsData,
    RadiologyInsightsInference,
    RadiologyInsightsInferenceOptions,
    RadiologyInsightsInferenceResult,
    RadiologyInsightsJob,
    RadiologyInsightsModelConfiguration,
    RadiologyInsightsPatientResult,
    RadiologyProcedureInference,
    Range,
    Ratio,
    RecommendationFinding,
    Reference,
    Resource,
    SampledData,
    ScoringAndAssessmentInference,
    SexMismatchInference,
    TimePeriod,
)

from ._enums import (  # type: ignore
    ClinicalDocumentType,
    ContactPointSystem,
    ContactPointUse,
    DocumentContentSourceType,
    DocumentType,
    EncounterClass,
    GuidanceRankingType,
    JobStatus,
    LateralityDiscrepancyType,
    MedicalProfessionalType,
    ObservationStatusCodeType,
    PatientSex,
    QualityMeasureComplianceType,
    QualityMeasureType,
    RadiologyInsightsInferenceType,
    RecommendationFindingStatusType,
    ResearchStudyStatusCodeType,
    ScoringAndAssessmentCategoryType,
    SpecialtyType,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AgeMismatchInference",
    "Annotation",
    "AssessmentValueRange",
    "CodeableConcept",
    "Coding",
    "CompleteOrderDiscrepancyInference",
    "CriticalResult",
    "CriticalResultInference",
    "DocumentAdministrativeMetadata",
    "DocumentAuthor",
    "DocumentContent",
    "DomainResource",
    "Element",
    "Extension",
    "FindingInference",
    "FindingOptions",
    "FollowupCommunicationInference",
    "FollowupRecommendationInference",
    "FollowupRecommendationOptions",
    "GenericProcedureRecommendation",
    "GuidanceInference",
    "GuidanceOptions",
    "HealthInsightsErrorResponse",
    "Identifier",
    "ImagingProcedure",
    "ImagingProcedureRecommendation",
    "LateralityDiscrepancyInference",
    "LimitedOrderDiscrepancyInference",
    "Meta",
    "Narrative",
    "Observation",
    "ObservationComponent",
    "ObservationReferenceRange",
    "OrderedProcedure",
    "PatientDetails",
    "PatientDocument",
    "PatientEncounter",
    "PatientRecord",
    "Period",
    "PresentGuidanceInformation",
    "ProcedureRecommendation",
    "QualityMeasureInference",
    "QualityMeasureOptions",
    "Quantity",
    "RadiologyCodeWithTypes",
    "RadiologyInsightsData",
    "RadiologyInsightsInference",
    "RadiologyInsightsInferenceOptions",
    "RadiologyInsightsInferenceResult",
    "RadiologyInsightsJob",
    "RadiologyInsightsModelConfiguration",
    "RadiologyInsightsPatientResult",
    "RadiologyProcedureInference",
    "Range",
    "Ratio",
    "RecommendationFinding",
    "Reference",
    "Resource",
    "SampledData",
    "ScoringAndAssessmentInference",
    "SexMismatchInference",
    "TimePeriod",
    "ClinicalDocumentType",
    "ContactPointSystem",
    "ContactPointUse",
    "DocumentContentSourceType",
    "DocumentType",
    "EncounterClass",
    "GuidanceRankingType",
    "JobStatus",
    "LateralityDiscrepancyType",
    "MedicalProfessionalType",
    "ObservationStatusCodeType",
    "PatientSex",
    "QualityMeasureComplianceType",
    "QualityMeasureType",
    "RadiologyInsightsInferenceType",
    "RecommendationFindingStatusType",
    "ResearchStudyStatusCodeType",
    "ScoringAndAssessmentCategoryType",
    "SpecialtyType",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
