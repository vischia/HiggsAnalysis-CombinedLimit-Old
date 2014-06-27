from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class HeavyChHiggs(PhysicsModel):
    "Cross section: xsec. Branching ratios: Btaunu, Btb."
    def __init__(self):
        #      	SMLikeHiggsModel.__init__(self) # not using 'super(x,self).__init__' since I don't understand it
       	PhysicsModel.__init__(self) 
    def setPhysicsOptions(self,physOptions):
       	pass
    def doParametersOfInterest(self):
       	"""Create POI out of signal strength and MH"""
       	# --- Three parameters, xsec, Btaunu and Btb, with starting value 1 and range 0 to 20 ---
        # --- This is nasty case in which you do want to estimate the relative strength
        #       	self.modelBuilder.doVar("xsec[1,0,20]")
        #       	self.modelBuilder.doVar("Btaunu[1,0,20]")
        #       	self.modelBuilder.doVar("Btb[1,0,20]")
       	# --- declare that mu and theta are parameters of interest of the model
        #       	self.modelBuilder.doSet('POI','xsec,Btaunu,Btb')
       	# --- define products
       	#self.modelBuilder.factory_("prod::xsec_times_Btaunu(xsec,Btaunu)")
        #self.modelBuilder.factory_("prod::xsec_times_Btb(xsec,Btb)")
        #self.modelBuilder.factory_('expr::Scaling_HTB("@0", xsec_times_Btb)')
        #self.modelBuilder.factory_('expr::Scaling_TBH("@0", xsec_times_Btaunu)')

       	# --- Two parameters: xsectimesBtaunu and xsectimesBtb, with starting value 1 and range 0 to 20 ---
        self.modelBuilder.doVar("r_HTB[0.,0.,1.]")
        self.modelBuilder.doVar("r_TBH[0.,0.,1.]")
       	# --- declare that mu and theta are parameters of interest of the model
        self.modelBuilder.doSet('POI','r_HTB,r_TBH')
       	# --- define products
       	self.modelBuilder.factory_('expr::Scaling_HTB("@0", r_HTB)')
        self.modelBuilder.factory_('expr::Scaling_TBH("@0", r_TBH)')

        self.processScaling = { 'HTB':'HTB', 'TBH':'TBH' }

                      
    def getYieldScale(self,bin,process):
        for prefix, model in self.processScaling.iteritems():
            if process.startswith(prefix):
                return 'Scaling_'+model
        return 1


heavych = HeavyChHiggs()

class MSSMHeavyChHiggs(PhysicsModel):
    "Cross section: xsec. Branching ratios: already scaled in datacards creation."
    def __init__(self):
        PhysicsModel.__init__(self)
    def setPhysicsOptions(self, physOptions):
        pass
    def doParametersOfInterest(self):
        """Create POI out of signal strength and assign it to both channels"""
        # One parameter (xsec)
        self.modelBuilder.doVar('XSEC[1,0,10]');
        # Declare it parameter of interest
        self.modelBuilder.doSet('POI','XSEC')
        # Define scaling for HTB and TBH
        self.modelBuilder.factory_('expr::Scaling_HTB("@0", XSEC)')
        self.modelBuilder.factory_('expr::Scaling_TBH("@0", XSEC)')

        self.processScaling = { 'HTB':'HTB', 'TBH':'TBH'}

    def getYieldScale(self,bin,process):
        for prefix, model in self.processScaling.iteritems():
            if process.startswith(prefix):
                return 'Scaling_'+model
        return 1    

mssmheavych = MSSMHeavyChHiggs()
