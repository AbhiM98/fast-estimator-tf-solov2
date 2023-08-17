# Copyright 2019 The FastEstimator Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from typing import TYPE_CHECKING

import lazy_loader as lazy

__getattr__, __dir__, __all__ = lazy.attach(__name__,
                                            submod_attrs={'eigen_cam': ['EigenCAM'],
                                                          'grad_cam': ['GradCAM'],
                                                          'instance_tracker': ['InstanceTracker'],
                                                          'label_tracker': ['LabelTracker'],
                                                          'saliency': ['Saliency'], })

if TYPE_CHECKING:
    from fastestimator.trace.xai.eigen_cam import EigenCAM
    from fastestimator.trace.xai.grad_cam import GradCAM
    from fastestimator.trace.xai.instance_tracker import InstanceTracker
    from fastestimator.trace.xai.label_tracker import LabelTracker
    from fastestimator.trace.xai.saliency import Saliency
