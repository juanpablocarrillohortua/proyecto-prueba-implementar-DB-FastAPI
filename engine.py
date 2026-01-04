from sqlmodel import create_engine

mysql_url = "mysql+pymysql://root:@localhost:3306/heroes"
engine = create_engine(mysql_url, echo=True)