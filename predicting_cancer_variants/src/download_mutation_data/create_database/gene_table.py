from abc import ABC

from predicting_cancer_variants.src.download_mutation_data.create_database.table import Table


# Inherit from Table abstract base class
class GeneTable(Table, ABC):

    @property
    def _table_name(self):
        return self._configuration.database_table_name_gene

    @property
    def _create_table_segment(self):
        return """         
                (
                   entrezGeneId     INTEGER
                  ,hugoGeneSymbol   VARCHAR(30)
                  ,type             VARCHAR(30)
                )
        """
