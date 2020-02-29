from predicting_cancer_variants.src.common.configuration import Configuration
from predicting_cancer_variants.src.download_mutation_data import create_database_controller, download_controller


class MainController:
    logger = Configuration().get_logger(__name__)
    try:
        logger.info("Starting predicting_cancer_variants")

        create_database_controller.run()
        download_controller.run()

        logger.info("predicting_cancer_variants complete")

    except Exception as e:
        message = "predicting_cancer_variants has failed"
        logger.exception(message, exc_info=e)
        raise SystemExit(message)


