from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Lm_RoofWindows_FHEM(AliceSkill):
	"""
	Author: milode
	Description: Oeffnen und schliessen der dachfenster ueber fhem
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
