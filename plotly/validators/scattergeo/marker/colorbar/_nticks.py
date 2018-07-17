import _plotly_utils.basevalidators


class NticksValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self,
        plotly_name='nticks',
        parent_name='scattergeo.marker.colorbar',
        **kwargs
    ):
        super(NticksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=0,
            role='style',
            **kwargs
        )