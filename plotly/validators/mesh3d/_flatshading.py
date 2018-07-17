import _plotly_utils.basevalidators


class FlatshadingValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='flatshading', parent_name='mesh3d', **kwargs
    ):
        super(FlatshadingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            **kwargs
        )