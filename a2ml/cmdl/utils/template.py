import os
import shutil

class Template(object):

    @staticmethod
    def copy_config_files(experiment_path, providers):
        module_path = os.path.dirname(os.path.abspath(__file__))
        for provider in providers:
            src_config = os.path.abspath(os.path.join(
                module_path, '../template/%s.yaml' % provider))
            dest_config = os.path.join(experiment_path, '%s.yaml' % provider)
            shutil.copy2(src_config, dest_config)
        src_config = os.path.abspath(os.path.join(
            module_path, '../template/get_data.template'))
        dest_config = os.path.join(experiment_path, 'get_data.template')
        shutil.copy2(src_config,dest_config)
