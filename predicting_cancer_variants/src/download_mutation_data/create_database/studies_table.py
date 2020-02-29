from abc import ABC

from predicting_cancer_variants.src.download_mutation_data.create_database.table import Table


# Inherit from Table abstract base class
class StudiesTable(Table, ABC):

    @property
    def _table_name(self):
        return self._configuration.database_table_name_study

    @property
    def _create_table_segment(self):
        return """         
                (
                     studyID                VARCHAR(100) NOT NULL PRIMARY KEY
                     ,name                  VARCHAR(200) NOT NULL
                     ,shortName             VARCHAR(200) 
                     ,description           VARCHAR(200)
                     ,publicStudy           INTEGER
                     ,pmID                  VARCHAR(60) 
                     ,groups                VARCHAR(200)
                     ,citation              VARCHAR(300)
                     ,status                VARCHAR(200)
                     ,importDate            DATETIME
                     ,allSampleCount        INTEGER
                     ,cancerTypeId          VARCHAR(5)
                     ,referenceGenome       VARCHAR(10)
                )
        """
