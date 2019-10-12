Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname>, <lastname> and <homephone>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | firstname  | lastname  | homephone  |
    | firstname1 | lastname1 | homephone1 |
    | firstname2 | lastname2 | homephone2 |

Scenario: Modify a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I modify a contact from the list
    Then the new list is equal to the old list with modified contact

Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete a contact from the list
    Then the new list is equal to the old list without the deleted contact
