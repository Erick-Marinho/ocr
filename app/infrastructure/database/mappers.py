from app.domain.models import OcrResult as DomainOcrResult
from app.infrastructure.database.orm import OcrResult as OrmOcrResult

class OcrResultMapper:
    @staticmethod
    def to_domain(orm_entity: OrmOcrResult) -> DomainOcrResult:
        return DomainOcrResult(
            id=orm_entity.id,
            filename=orm_entity.filename,
            extracted_text=orm_entity.extracted_text,
            created_at=orm_entity.created_at,
            updated_at=orm_entity.updated_at
        )
    
    @staticmethod
    def to_orm(domain_entity: DomainOcrResult) -> OrmOcrResult:
        return OrmOcrResult(
            filename=domain_entity.filename,
            extracted_text=domain_entity.extracted_text
        )