from SpiffWorkflow.specs import Simple

from SpiffWorkflow.bpmn.specs.BpmnSpecMixin import BpmnSpecMixin


class BusinessRuleTask(Simple, BpmnSpecMixin):
    """
    Task Spec for a bpmn:businessTask (DMB Decision Reference) node.
    """

    def _on_trigger(self, my_task):
        pass

    def __init__(self, wf_spec, name, dmnEngine=None, **kwargs):
        super().__init__(wf_spec, name, **kwargs)

        self.dmnEngine = dmnEngine
        self.res = None
        self.resDict = None

    def _on_complete_hook(self, my_task):
        self.res = self.dmnEngine.decide(**my_task.data)
        self.resDict = self.res.outputAsDict()
        my_task.data.update(self.resDict)
        super(BusinessRuleTask, self)._on_complete_hook(my_task)
        my_task.workflow.data.update(self.resDict)
