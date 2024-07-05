в таблицу описанную моделью 
class Model1(Base):
    __tablename__ = "pledgeSecurities"
    __table_args__ = {'extend_existing': True}

    id: Mapped[intpk]
    file_id: Mapped[int]
    pledge_type_id: Mapped[int]
    sb_id: Mapped[str_50]
    security_name: Mapped[Optional[str]]
    collateral_val_amt: Mapped[Optional[num_22_2]]
    createdAt: Mapped[created_at]
    updatedAt: Mapped[updated_at]

записываю датафрейм с атрибутами
file_id: Mapped[int]
pledge_type_id: Mapped[int]
sb_id: Mapped[str_50]
security_name: Mapped[Optional[str]]   
collateral_val_amt: Mapped[Optional[num_22_2]]

через df.to_sql()
возникает ошибка:
"detail": "(psycopg2.errors.NotNullViolation) null value in column \"createdAt\" of relation \"commonAttributes\" violates not-null constraint
