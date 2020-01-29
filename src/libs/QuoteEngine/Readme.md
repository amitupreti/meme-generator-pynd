NAME

    libs.QuoteEngine

PACKAGE CONTENTS

    Ingestor
    QuoteEngine

Package Dependencies
     
     pandas
     python-docx
     

## class Ingestor(libs.QuoteEngine.Interface.IngestorInterface)
     
    Main Ingestor that can automatically parse the supported file types
 
    Class methods defined here:
 
       parse(path: str) -> List[libs.QuoteEngine.QuoteEngine.QuoteModel] from abc.ABCMeta
     
           Parses the given file if it is supported and Returns the QuoteModel Object.
           :param path: path to file
           :return: QuoteModel object
 

       can_ingest(path)
           Checks if the file type is supported by our Ingestor.
 
 
 

### Example of using Ingestor
```python
quote_file = './_data/DogQuotes/DogQuotesCSV.csv'
quotes = Ingestor.parse(quote_file)
```

## class QuoteModel(builtins.object)

    QuoteModel(body, author)
    Quote Model class that creates the default formatting for quotes.

 
 
### Example of using QuoteModel
```python
body  = "Sleep like its the end"
author = 'Anon'
QuoteObject = QuoteModel(body, author)
```
