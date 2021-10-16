const ColorChanger = require("./ColorChanger")

// @ponicode
describe("handleChangeColor", () => {
    let object
    let inst

    beforeEach(() => {
        object = [["Edmond", "Michael", "Jean-Philippe"], ["Anas", "George", "Michael"], ["Michael", "Pierre Edouard", "Edmond"]]
        inst = new ColorChanger.default(object)
    })

    test("0", () => {
        let callFunction = () => {
            inst.handleChangeColor({ target: { value: "elio@example.com" } })
        }
    
        expect(callFunction).not.toThrow()
    })

    test("1", () => {
        let callFunction = () => {
            inst.handleChangeColor({ target: { value: "Dillenberg" } })
        }
    
        expect(callFunction).not.toThrow()
    })

    test("2", () => {
        let callFunction = () => {
            inst.handleChangeColor({ target: { value: "Elio" } })
        }
    
        expect(callFunction).not.toThrow()
    })

    test("3", () => {
        let callFunction = () => {
            inst.handleChangeColor(undefined)
        }
    
        expect(callFunction).not.toThrow()
    })
})
