from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database engine
engine = create_engine('sqlite:///bookcatalogswithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Muneera AlRashidi", email="muneera@protonmail.com")
session.add(User1)
session.commit()

# Create books Categories
category1 = Categories(user_id=1, name="Biographies & Memoirs")
session.add(category1)
session.commit()


category2 = Categories(user_id=1, name="Literature & Fiction")
session.add(category2)
session.commit()

category3 = Categories(user_id=1, name="Children's Books")
session.add(category3)
session.commit()

category4 = Categories(user_id=1, name="Arts & Photography")
session.add(category4)
session.commit()

category5 = Categories(user_id=1, name="Non-Fiction")
session.add(category5)
session.commit()


# Add books into categories
categoryItem1 = CategoryItem(user_id=1, name="Educated",
                             description="An unforgettable memoir about \
                             a young girl who, kept out of school, \
                             leaves her survivalist family and \
                             goes on to earn a PhD \
                             Cambridge University",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="1984",
                             description="In 1984, London is a grim \
                             city in the totalitarian \
                             state of Oceania where Big Brother\
                              is always watching you \
                              and the Thought Police can \
                              practically read your mind. \
                              Winston Smith is a man in grave danger\
                               for the simple \
                              reason that his memory still functions. \
                              Drawn into a forbidden love affair, Winston \
                              finds the courage to join \
                              a secret revolutionary \
                              organization called The Brotherhood,\
                               dedicated to \
                              the destruction of the Party. \
                              Together with his beloved Julia,\
                               he hazards his \
                              life in a deadly match against\
                               the powers that be.",
                             categories=category2)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="A Wrinkle in Time",
                             description="A Wrinkle in Time is the story of \
                             Meg Murry, a high-school-aged girl \
                              who is transported on an adventure through \
                              time and space with her younger \
                              brother Charles Wallace \
                              and her friend Calvin O'Keefe to \
                              rescue her father, \
                              a gifted scientist, \
                              from the evil forces that \
                              hold him prisoner \
                              on another planet.",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Beastie Boys Book",
                             description="Beastie Boys Book upends \
                             the typical music memoir. \
                              Alongside the band narrative you will \
                              find rare photos, original illustrations, \
                              a cookbook by chef Roy Choi, a graphic novel, \
                              a map of Beastie Boys New York, \
                              mixtape playlists, pieces by guest \
                              contributors, and many more surprises.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Thinking, Fast and Slow ",
                             description="Thinking, Fast and Slow is \
                             a best-selling book published in 2011 \
                             by Nobel Memorial Prize in Economic Sciences \
                             laureate Daniel Kahneman. \
                             The book summarizes research that Kahneman \
                             conducted over decades. It covers all three \
                             phases of his career: \
                             his early days working on \
                             cognitive biases, his work on \
                             prospect theory, and his \
                             later work on happiness",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Becoming",
                             description="An intimate, powerful, \
                             and inspiring memoir by \
                             the former First Lady of the United States \
                             Michelle Obama invites readers into her world, \
                             chronicling the experiences \
                             that have shaped her, \
                             from her childhood on the \
                             South Side of Chicago to \
                             her years as an executive \
                             balancing the demands of \
                             motherhood and work, \
                             to her time spent at the \
                             world most famous address",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Fahrenheit 451",
                             description="Ray Bradburys internationally \
                             acclaimed novel Fahrenheit 451 \
                             is a masterwork of twentieth-century literature \
                             set in a bleak, dystopian future.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Waiting Is Not Easy!",
                             description="A story about an elephant \
                             and piggie book",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Power of Now",
                             description="The Power of Now: A Guide \
                             to Spiritual Enlightenment \
                              takes readers on an inspiring \
                              spiritual journey to find \
                              their true and deepest self \
                              and reach the ultimate in personal \
                              growth and spirituality: the discovery \
                              of truth and light.",
                             categories=category5)
session.add(categoryItem1)
session.commit()


print "added catalog items!"
