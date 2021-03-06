"""! 
@brief Example 12
@details pyAudioAnalysis feature extraction for classes organized in folders
and feature histogram representation (per feature and class).
Binary classification task: male vs female speech segments
@author Theodoros Giannakopoulos {tyiannak@gmail.com}
"""
from pyAudioAnalysis import MidTermFeatures as aF
import os.path
import utilities as ut

if __name__ == '__main__':
    dirs = ["../data/gender/male",
            "../data/gender/female"]
    class_names = [os.path.basename(d) for d in dirs]
    m_win, m_step, s_win, s_step = 1, 1, 0.1, 0.05
    features = []
    for d in dirs:
        # get feature matrix for each directory (class)
        f, files, fn = aF.directory_feature_extraction(d, m_win, m_step, s_win,
                                                       s_step)
        features.append(f)
    ut.plot_feature_histograms(features, fn, class_names)