from unittest import TestCase

from project.team import Team


class TeamTest(TestCase):

    def setUp(self):
        self.team = Team('Danio')

    def test__init__(self):
        self.assertEqual('Danio', self.team.name)
        self.assertEqual({}, self.team.members)

    def test__name_with_digit_char__expect_raises(self):
        with self.assertRaises(ValueError) as ve:
            Team('Dan4o')

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_members__expect__ok(self):
        self.assertEqual({}, self.team.members)
        members = {'lildanio': 12}
        self.assertEqual(f"Successfully added: lildanio", self.team.add_member(**members))
        self.assertEqual({'lildanio': 12}, self.team.members)

        members2 = {'lilgosho': 14, 'lilpish': 15}
        self.assertEqual(f"Successfully added: lilgosho, lilpish", self.team.add_member(**members2))
        self.assertEqual({'lildanio': 12, 'lilgosho': 14, 'lilpish': 15}, self.team.members)

    def test_add_existing_member__expect_raises(self):
        self.assertEqual({}, self.team.members)
        members = {'lildanio': 12}
        self.assertEqual(f"Successfully added: lildanio", self.team.add_member(**members))
        self.assertEqual({'lildanio': 12}, self.team.members)

        self.assertEqual("Successfully added: ", self.team.add_member(**members))

    def test_remove_member_that_is_in_members(self):
        members = {'lildanio': 12}
        self.team.add_member(**members)
        self.assertEqual({'lildanio': 12}, self.team.members)

        self.assertEqual("Member lildanio removed", self.team.remove_member('lildanio'))
        self.assertEqual({}, self.team.members)

        self.assertEqual('Member with name lildanio does not exist', self.team.remove_member('lildanio'))

    def test_gt_(self):
        second_team = Team('teammm')
        members_2 = {'lilshet': 12, 'lildump': 18}
        second_team.add_member(**members_2)

        self.assertEqual(True, len(second_team) > len(self.team))

        members_1 = {'lildog': 29, 'lildigg': 16}
        self.team.add_member(**members_1)

        self.assertEqual(False, len(second_team) > len(self.team))

    def test__len(self):
        members_1 = {'lildog': 29, 'lildigg': 16}
        self.team.add_member(**members_1)
        self.assertEqual(2, len(self.team))

    def test_add_team(self):
        self.team.members = {'lildog': 29, 'lildigg': 16}

        second_team = Team('shet')
        second_team.members = {'lilpick': 21, 'lilshet': 26}

        merged_team = self.team + second_team
        self.assertEqual('Danioshet', merged_team.name)

        self.assertEqual({'lildog': 29, 'lildigg': 16, 'lilpick': 21, 'lilshet': 26}, merged_team.members)

    def test_str_(self):
        self.team.members = {'lildog': 29, 'ekko': 21, 'divane': 21, 'lilshet': 26}
        result = ["Team name: Danio\n"]
        result.extend("Member: lildog - 29-years old\nMember: lilshet - 26-years old\nMember: divane - 21-years old\nMember: ekko - 21-years old")

        self.assertEqual(''.join(result), str(self.team))
