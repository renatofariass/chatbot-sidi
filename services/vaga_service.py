from entities.vaga import Vaga


def check_job_id(self):
    vaga = Vaga.query.filter_by(job_id=self).first()
    if not vaga:
        return False
    if vaga:
        return True