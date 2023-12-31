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
                                            submod_attrs={'early_stopping': ['EarlyStopping'],
                                                          'lr_scheduler': ['LRScheduler'],
                                                          'pbm_calibrator': ['PBMCalibrator'],
                                                          'reduce_lr_on_plateau': ['ReduceLROnPlateau'],
                                                          'terminate_on_nan': ['TerminateOnNaN'], })

if TYPE_CHECKING:
    from fastestimator.trace.adapt.early_stopping import EarlyStopping
    from fastestimator.trace.adapt.lr_scheduler import LRScheduler
    from fastestimator.trace.adapt.pbm_calibrator import PBMCalibrator
    from fastestimator.trace.adapt.reduce_lr_on_plateau import ReduceLROnPlateau
    from fastestimator.trace.adapt.terminate_on_nan import TerminateOnNaN
