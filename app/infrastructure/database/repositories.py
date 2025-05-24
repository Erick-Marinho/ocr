from sqlalchemy.orm import Session
from app.domain.repositories import IOcrResultRepository
from app.domain.models import OcrResult as DomainOcrResult
from app.infrastructure.database.mappers import OcrResultMapper
from app.infrastructure.database.orm import OcrResult as OrmOcrResult

class SqlAlchemyOcrRepository(IOcrResultRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def save(self, ocr_result: DomainOcrResult) -> DomainOcrResult:
        orm_instance = OcrResultMapper.to_orm(ocr_result)

        self.db.add(orm_instance)
        self.db.commit()
        self.db.refresh(orm_instance)

        return OcrResultMapper.to_domain(orm_instance)
    
    def find_by_id(self, result_id: int) -> DomainOcrResult | None:
        orm_instance = self.db.query(OrmOcrResult).filter(OrmOcrResult.id == result_id).first()

        if orm_instance:
            return OcrResultMapper.to_domain(orm_instance)
        
        return None