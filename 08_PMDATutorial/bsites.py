from __future__ import absolute_import, division

import numpy as np

from pmda.parallel import ParallelAnalysisBase

class bsites_finder(ParallelAnalysisBase):
    """Bingding sites finder for MD simulaton trajectory
    
    Arguments
    ---------
    u : Universe
          a Universe that contains g1 and g2.
    g1 : AtomGroup
          Target atoms.
    g2 : AtomGroup
          Potential binding sites.
    cutoff : int (optional)
          Maximum of the distance between ions and binding sites
    """
    def __init__(self, u, g1, g2, cutoff=5.0):
        super(bsites_finder, self).__init__(u, (g1, g2))
        self.cutoff=cutoff
 
    def _prepare(self):
        self.ids = None

    def _single_frame(self, ts, atomgroups):
        g1, g2 = atomgroups
        ag = g1+g2
        # Generate selection strings for ions and binding sites
        id1 = ' '.join(str(id) for id in g1.resids)
        id2 = ' '.join(str(id) for id in g2.resids)
        # Generate AtomGroup of binding sites
        sites = ag.select_atoms('resid {0} and around {1} (resid {2})'.format(
               id1, self.cutoff, id2))
        # Generate the list of the resids of binding sites
        ids = np.unique(np.array(sites.residues.ix))
        return ids

    def _conclude(self,):
        self.ids = np.array([])
        for result in self._results:
            self.ids = np.append(self.ids, result)

    @staticmethod
    def _reduce(res, result_single_frame):
        if isinstance(res, list) and len(res) == 0:
            # Initialization of the result
            # Convert res from an empty list to a numpy array
            # which has the same shape as the single frame result
            res = result_single_frame
        else:
            # Append new single frame result to res
            res = np.append(res, result_single_frame)
        return res
