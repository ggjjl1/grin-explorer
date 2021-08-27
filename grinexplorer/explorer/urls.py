from django.urls import path

from .charts import block_chart, fee_chart
from .views import BlockList, BlocksByHeight, BlockDetail, OutputByCommit, Search

urlpatterns = [
    path("", BlockList.as_view(), name="block-list"),
    path("chart/block", block_chart, name="block-chart"),
    path("chart/fee", fee_chart, name="fee-chart"),
    path("block/<int:height>", BlocksByHeight.as_view(), name="blocks-by-height"),
    path("block/<str:pk>", BlockDetail.as_view(), name="block-detail"),
    path("output/<str:commit>", OutputByCommit.as_view(), name="output-detail"),
    path("search", Search.as_view(), name="search"),
]
